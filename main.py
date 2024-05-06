import random
from gemini_ai import generate_response
from imageEdit import add_text_to_image
from instagramBot import upload_photo_to_instagram

def create_quote_post():
    # List of famous people
 
    famous_people = [
    "Jay-Z",
    "Elon Musk",
    "Jeff Bezos",
    "Maya Angelou",
    "Albert Einstein",
    "William Shakespeare",
    "Coco Chanel",
    "Nikola Tesla",
    "Rumi",
    "Oprah Winfrey",
    "Marie Curie",
    "Rabindranath Tagore",
    "Mark Zuckerberg",
    "Stephen Hawking",
    "Emily Dickinson",
    "Leonardo da Vinci",
    "Sylvia Plath",
    "Issac Newton",
    "Pablo Neruda",
    "Frida Kahlo",
    "Galileo Galilei",
    "Langston Hughes",
    "Ada Lovelace",
    "Walt Whitman",
    "Sigmund Freud",
    "Edgar Allan Poe",
    "Jane Austen",
    "Helen Keller",
    "Vincent Van Gogh",
    "T.S. Eliot",
    "Grace Hopper",
    "Emily Bronte",
    "Carl Sagan",
    "Marilyn Monroe",
    "Pierre Teilhard de Chardin",
    "Fyodor Dostoevsky",
    "Margaret Atwood",
    "Steve Jobs",
    "Charles Darwin",
    "Emily Dickinson",
    "Aristotle",
    "Virginia Woolf",
    "Nelson Mandela",
    "Ada Lovelace",
    "Stephen King",
    "Homer",
    "Martha Graham",
    "Martin Luther King Jr.",
    "Alan Turing",
    "J.K. Rowling",
    "Khalil Gibran",
    "Harriet Tubman",
    "Richard Feynman",
    "Emily Dickinson",
    "Haruki Murakami",
    "Mother Teresa",
    "Michelangelo",
    "John Lennon",
    "Mary Shelley",
    "George Orwell",
    "Simone de Beauvoir",
    "Margaret Mead",
    "Paulo Coelho",
    "Hedy Lamarr",
    "John Keats",
    "Katherine Johnson",
    "Heraclitus",
    "Plato",
    "Ernest Hemingway",
    "W.E.B. Du Bois",
    "Roald Dahl",
    "Louisa May Alcott",
    "Friedrich Nietzsche",
    "James Joyce",
    "Rosalind Franklin",
    "Harper Lee",
    "Gustave Flaubert",
    "H.G. Wells",
    "Albert Camus",
    "J.R.R. Tolkien",
    "Emily Dickinson",
    "Leonardo da Vinci",
    "Simone Weil",
    "Vincent Van Gogh",
    "Emily Dickinson",
    "Albert Schweitzer",
    "Walt Disney",
    "Jorge Luis Borges",
    "Emily Dickinson",
    "George Eliot",
    "Carl Jung",
    "Emily Dickinson",
    "Winston Churchill",
    "Emily Dickinson",
    "Benjamin Franklin",
    "Emily Dickinson"
]
    
    # Choose a random author
    author = random.choice(famous_people)
    
    # Construct input text
    input_text = f"write a quote of {author} and mention the author name"
    
    # Generate response using Gemini AI
    response = generate_response(input_text)
    
    # Add text to image
    add_text_to_image(text=response)
    
    # Upload photo to Instagram
    upload_photo_to_instagram(file_path='post.png', caption=response)

# Example usage

