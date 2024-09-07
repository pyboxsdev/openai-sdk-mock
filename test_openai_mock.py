import unittest
from openai_mock import openai

class TestOpenAIMock(unittest.TestCase):

    def test_chat_completion(self):
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": "Hello, how are you?"}]
        response = openai.ChatCompletion.create(model=model, messages=messages)
        
        self.assertIn("Hello, how are you?", response["choices"][0]["message"]["content"])
        self.assertIn(model, response["choices"][0]["message"]["content"])
        self.assertEqual(response["model"], model)

    def test_completion(self):
        model = "text-davinci-002"
        prompt = "Translate the following English text to French: 'Hello, how are you?'"
        response = openai.Completion.create(model=model, prompt=prompt)
        
        self.assertIn(prompt, response["choices"][0]["text"])
        self.assertIn(model, response["choices"][0]["text"])
        self.assertEqual(response["model"], model)

    def test_embedding(self):
        model = "text-embedding-ada-002"
        input_text = "The quick brown fox jumps over the lazy dog"
        response = openai.Embedding.create(model=model, input=input_text)
        
        self.assertEqual(response["object"], "list")
        self.assertEqual(len(response["data"]), 1)
        self.assertEqual(len(response["data"][0]["embedding"]), 16)  # We now have 16 values in our mock
        self.assertEqual(response["model"], model)
        self.assertEqual(response["usage"]["prompt_tokens"], len(input_text.split()))

    def test_model_list(self):
        response = openai.Model.list()
        self.assertEqual(response["object"], "list")
        self.assertTrue(len(response["data"]) > 0)
        self.assertIn("gpt-4", [model["id"] for model in response["data"]])
        self.assertIn("gpt-3.5-turbo", [model["id"] for model in response["data"]])

    def test_model_retrieve(self):
        model = "gpt-3.5-turbo"
        response = openai.Model.retrieve(model)
        self.assertEqual(response["id"], model)
        self.assertEqual(response["object"], "model")
        self.assertEqual(response["owned_by"], "openai")

        with self.assertRaises(ValueError):
            openai.Model.retrieve("non-existent-model")

    def test_file(self):
        file_response = openai.File.create(file="dummy_file", purpose="fine-tune")
        self.assertEqual(file_response["object"], "file")
        self.assertEqual(file_response["purpose"], "fine-tune")

        list_response = openai.File.list()
        self.assertEqual(list_response["object"], "list")
        self.assertTrue(len(list_response["data"]) > 0)

        delete_response = openai.File.delete("file-mock123")
        self.assertTrue(delete_response["deleted"])

    def test_image(self):
        create_response = openai.Image.create(prompt="A beautiful sunset", n=2)
        self.assertEqual(len(create_response["data"]), 2)
        self.assertTrue(all("url" in item for item in create_response["data"]))

        edit_response = openai.Image.create_edit(image="dummy_image", prompt="Add a bird", n=1)
        self.assertEqual(len(edit_response["data"]), 1)
        self.assertTrue("url" in edit_response["data"][0])

        variation_response = openai.Image.create_variation(image="dummy_image", n=3)
        self.assertEqual(len(variation_response["data"]), 3)
        self.assertTrue(all("url" in item for item in variation_response["data"]))

    def test_moderation(self):
        response = openai.Moderation.create(input="Some text to moderate")
        self.assertEqual(response["model"], "text-moderation-001")
        self.assertTrue("results" in response)
        self.assertFalse(response["results"][0]["flagged"])

    def test_organization(self):
        response = openai.Organization.list()
        self.assertEqual(response["object"], "list")
        self.assertTrue(len(response["data"]) > 0)
        self.assertEqual(response["data"][0]["object"], "organization")

    def test_thread(self):
        create_response = openai.Thread.create()
        self.assertEqual(create_response["object"], "thread")

        thread_id = create_response["id"]
        retrieve_response = openai.Thread.retrieve(thread_id)
        self.assertEqual(retrieve_response["id"], thread_id)

        delete_response = openai.Thread.delete(thread_id)
        self.assertTrue(delete_response["deleted"])

if __name__ == '__main__':
    unittest.main()