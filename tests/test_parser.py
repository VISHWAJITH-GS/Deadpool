import unittest
from app.agent.intent_parser import intent_parser

class TestIntentParser(unittest.TestCase):
    def test_open_basic(self):
        result = intent_parser.parse_intent("Open notepad")
        self.assertIsNotNone(result)
        self.assertEqual(len(result["steps"]), 1)
        self.assertEqual(result["steps"][0]["action"], "open_app")
        self.assertEqual(result["steps"][0]["app"], "notepad")

        result = intent_parser.parse_intent("Open Chrome")
        self.assertEqual(result["steps"][0]["app"], "Chrome")
        
        result = intent_parser.parse_intent("Open Microsoft Word")
        self.assertEqual(result["steps"][0]["app"], "Microsoft Word")
        
        result = intent_parser.parse_intent("Launch Microsoft Word")
        self.assertEqual(result["steps"][0]["app"], "Microsoft Word")
        
        result = intent_parser.parse_intent("Open Chrome app")
        self.assertEqual(result["steps"][0]["app"], "Chrome")
        
        result = intent_parser.parse_intent("Open Microsoft Word app")
        self.assertEqual(result["steps"][0]["app"], "Microsoft Word")

    def test_open_and_type(self):
        result = intent_parser.parse_intent("Open notepad and type I love You vishwajith")
        self.assertIsNotNone(result)
        self.assertEqual(len(result["steps"]), 2)
        self.assertEqual(result["steps"][0]["action"], "open_app")
        self.assertEqual(result["steps"][0]["app"], "notepad")
        self.assertEqual(result["steps"][1]["action"], "type_text")
        self.assertEqual(result["steps"][1]["text"], "I love You vishwajith")
        
        result2 = intent_parser.parse_intent("Open notepad and type hello")
        self.assertEqual(result2["steps"][1]["text"], "hello")
        
        result3 = intent_parser.parse_intent("Open Notepad and write Hello Vishwajith")
        self.assertEqual(result3["steps"][1]["text"], "Hello Vishwajith")

    def test_type_in_app(self):
        result = intent_parser.parse_intent("Type I love you in Notepad")
        self.assertIsNotNone(result)
        self.assertEqual(len(result["steps"]), 1)
        self.assertEqual(result["steps"][0]["action"], "type_text")
        self.assertEqual(result["steps"][0]["text"], "I love you")
        self.assertEqual(result["steps"][0]["target_app"], "Notepad")
        
        result = intent_parser.parse_intent("Write Hello World into Notepad")
        self.assertIsNotNone(result)
        self.assertEqual(result["steps"][0]["action"], "type_text")
        self.assertEqual(result["steps"][0]["text"], "Hello World")
        self.assertEqual(result["steps"][0]["target_app"], "Notepad")

    def test_open_and_goto(self):
        result = intent_parser.parse_intent("Open Chrome and go to leetcode.com")
        self.assertIsNotNone(result)
        self.assertEqual(len(result["steps"]), 2)
        self.assertEqual(result["steps"][0]["action"], "open_app")
        self.assertEqual(result["steps"][0]["app"], "Chrome")
        self.assertEqual(result["steps"][1]["action"], "open_url")
        self.assertEqual(result["steps"][1]["url"], "leetcode.com")

    def test_open_goto_and_search(self):
        result = intent_parser.parse_intent("Open Chrome, go to LeetCode and search for Two Sum")
        self.assertIsNotNone(result)
        self.assertEqual(len(result["steps"]), 3)
        self.assertEqual(result["steps"][0]["action"], "open_app")
        self.assertEqual(result["steps"][0]["app"], "Chrome")
        self.assertEqual(result["steps"][1]["action"], "open_url")
        self.assertEqual(result["steps"][1]["url"], "LeetCode")
        self.assertEqual(result["steps"][2]["action"], "search")
        self.assertEqual(result["steps"][2]["query"], "Two Sum")

if __name__ == '__main__':
    unittest.main()
