import asyncio
import unittest

from src.lighthouseweb3.functions.kavach_generate import generate


class TestGenerateMethod(unittest.TestCase):

    def test_generate_output_structure(self):
        async def _run():
            result = await generate(threshold=3, key_count=5)
            self.assertIn("masterKey", result)
            self.assertIn("keyShards", result)
            self.assertEqual(len(result["keyShards"]), 5)

        asyncio.run(_run())

    def test_generate_invalid_input(self):
        with self.assertRaises(ValueError):
            asyncio.run(generate(threshold=5, key_count=3))


