# chatbot_backend.py
import torch
import logging
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


class ChatBot:
    def __init__(self, model_name="microsoft/gpt2"):
        """
        Initialize chatbot with specified model
        Different models for different use cases:
        - gpt2: Simple but fast
        - microsoft/DialoGPT-medium: Good for conversations
        """
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.chatbot_pipeline = None
        self.conversation_history = []  # Store conversation as list of strings

        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def load_model(self):
        """Load the selected model"""
        try:
            self.logger.info(f"Loading model: {self.model_name}")

            if "DialoGPT" in self.model_name:
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
                if self.tokenizer.pad_token is None:
                    self.tokenizer.pad_token = self.tokenizer.eos_token
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_name, use_safetensors=True
                )
                self.chatbot_pipeline = None  # Will use custom generation
            else:
                # Use text-generation pipeline for GPT-2
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
                if self.tokenizer.pad_token is None:
                    self.tokenizer.pad_token = self.tokenizer.eos_token

                self.chatbot_pipeline = pipeline(
                    "text-generation",
                    model=self.model_name,
                    tokenizer=self.tokenizer,
                )

            self.logger.info("Model loaded successfully!")
            return True

        except Exception as e:
            self.logger.error(f"Error loading model: {str(e)}")
            return False

    def generate_response_dialo(self, user_input):
        """Generate response using DialoGPT-style models"""
        try:
            # Build conversation context from history
            conversation_text = ""
            for i, msg in enumerate(self.conversation_history):
                conversation_text += msg + self.tokenizer.eos_token

            # Add current user input
            conversation_text += user_input + self.tokenizer.eos_token

            # Tokenize the entire conversation
            encoded = self.tokenizer.encode_plus(
                conversation_text,
                return_tensors="pt",
                padding=True,
                return_attention_mask=True,
            )

            input_ids = encoded["input_ids"]
            attention_mask = encoded["attention_mask"]

            # Generate response
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    attention_mask=attention_mask,
                    max_length=1000,
                    num_beams=5,
                    no_repeat_ngram_size=3,
                    do_sample=True,
                    temperature=0.6,
                    pad_token_id=self.tokenizer.eos_token_id,
                )

            # Decode response
            response = self.tokenizer.decode(
                output[:, input_ids.shape[-1] :][0], skip_special_tokens=True
            )

            # Add to conversation history
            self.conversation_history.append(user_input)
            self.conversation_history.append(response)

            return response

        except Exception as e:
            self.logger.error(f"Error generating response: {str(e)}")
            return "Sorry, I encountered an error processing your message."

    def generate_response_pipeline(self, user_input):
        """Generate response using pipeline-based models"""
        try:
            # Build conversation context
            conversation_text = ""
            for msg in self.conversation_history:
                conversation_text += msg + "\n"

            # Add current user input
            conversation_text += user_input

            # Use pipeline for generation
            result = self.chatbot_pipeline(
                conversation_text,
                max_length=len(conversation_text.split()) + 50,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )

            # Extract the generated text
            full_response = result[0]["generated_text"]

            # Extract only the new response (remove the input context)
            response = full_response[len(conversation_text) :].strip()

            # Add to conversation history
            self.conversation_history.append(user_input)
            self.conversation_history.append(response)

            return response if response else "I'm not sure how to respond to that."

        except Exception as e:
            self.logger.error(f"Error generating response: {str(e)}")
            return "Sorry, I encountered an error processing your message."

    def get_response(self, user_input):
        """Main method to get chatbot response"""
        if not user_input.strip():
            return "Please enter a message."

        if self.chatbot_pipeline:
            return self.generate_response_pipeline(user_input)
        else:
            return self.generate_response_dialo(user_input)

    def reset_conversation(self):
        """Reset the conversation history"""
        self.conversation_history = []
