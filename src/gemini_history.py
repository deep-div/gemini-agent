from google.genai.types import Part, Content, UserContent

class ConversationBuilder:
    def build_with_user_content(self, user_text: str):
        responses = [
            UserContent(parts=[Part(text=user_text)]), # will get a role='user' automatically 
        ]
        return responses

    def build_with_content_only(self, model_text: str):
        responses = [
            Content(parts=[Part(text=model_text)], role='model')
        ]
        return responses

    def build_combined(self, user_text: str, model_text: str):
        responses = [
            UserContent(parts=[Part(text=user_text)]),
            Content(parts=[Part(text=model_text)], role='model')
        ]
        return responses
