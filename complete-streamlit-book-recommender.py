import streamlit as st
import random

books = [
    {
        "title": "Die With Zero",
        "author": "Bill Perkins",
        "genre": "Finance",
        "popularity": 70,
        "khe_favorite": True,
        "synopsis": "Die With Zero challenges traditional retirement planning, advocating for strategic spending to maximize life experiences. Perkins argues for balancing saving with enjoying life's pleasures, urging readers to invest in memorable experiences and relationships rather than accumulating wealth for its own sake.",
        "amazonLink": "https://amzn.to/41PZtUQ"
    },
    {
        "title": "The Wisdom of Insecurity",
        "author": "Alan Watts",
        "genre": "Philosophy",
        "popularity": 85,
        "khe_favorite": True,
        "synopsis": "Watts explores the nature of anxiety and insecurity in modern life, proposing that our constant pursuit of security paradoxically leads to more stress. He advocates for embracing uncertainty and living fully in the present moment as a path to true contentment and wisdom.",
        "amazonLink": "https://amzn.to/3oBDHWd"
    },
    {
        "title": "Difficult Conversations",
        "author": "Douglas Stone",
        "genre": "Communication",
        "popularity": 88,
        "khe_favorite": True,
        "synopsis": "This book provides a framework for handling challenging discussions in both personal and professional contexts. It offers practical strategies for navigating emotions, differing perceptions, and identity issues in conversations, helping readers transform potential conflicts into opportunities for growth and understanding.",
        "amazonLink": "https://amzn.to/41tn0uZ"
    },
    {
        "title": "The Seven Principles for Making Marriage Work",
        "author": "John Gottman",
        "genre": "Relationships",
        "popularity": 92,
        "khe_favorite": True,
        "synopsis": "Based on extensive research, Gottman outlines seven key principles for maintaining a healthy, long-lasting marriage. The book offers practical exercises and advice for improving communication, resolving conflicts, and fostering intimacy in relationships.",
        "amazonLink": "https://amzn.to/3oxQYiG"
    },
    {
        "title": "The Five Invitations",
        "author": "Frank Ostaseski",
        "genre": "Spirituality",
        "popularity": 75,
        "khe_favorite": True,
        "synopsis": "Drawing from his experience in end-of-life care, Ostaseski presents five essential insights about living fully in the face of death. The book encourages readers to embrace life's uncertainties, find meaning in suffering, and live with greater presence and compassion.",
        "amazonLink": "https://amzn.to/3H3oWlw"
    },
    {
        "title": "Multipliers",
        "author": "Liz Wiseman",
        "genre": "Leadership",
        "popularity": 85,
        "khe_favorite": True,
        "synopsis": "Wiseman explores the concept of leadership multipliers who amplify the capabilities of those around them. The book contrasts these with diminishers who drain intelligence and capability, offering strategies for becoming a multiplier and maximizing team potential.",
        "amazonLink": "https://amzn.to/3oAtYzL"
    },
    {
        "title": "Give and Take",
        "author": "Adam Grant",
        "genre": "Business",
        "popularity": 90,
        "khe_favorite": True,
        "synopsis": "Grant examines the impact of different reciprocity styles on success. He argues that givers, who contribute to others without expecting immediate returns, can achieve extraordinary results across various fields, challenging the notion that nice guys finish last.",
        "amazonLink": "https://amzn.to/3oxwjeP"
    },
    {
        "title": "The Soul of Money",
        "author": "Lynn Twist",
        "genre": "Finance",
        "popularity": 78,
        "khe_favorite": True,
        "synopsis": "Twist reframes our relationship with money, arguing that it can be a tool for positive change rather than a source of stress. She encourages readers to align their use of money with their core values, promoting a more fulfilling and impactful approach to personal finance.",
        "amazonLink": "https://amzn.to/3H5pLKR"
    },
    {
        "title": "From Strength to Strength",
        "author": "Arthur C. Brooks",
        "genre": "Self-Help",
        "popularity": 82,
        "khe_favorite": True,
        "synopsis": "Brooks addresses the challenges of transitioning from success driven by fluid intelligence to wisdom-based achievements in later life. He offers strategies for finding meaning and happiness in the second half of life, emphasizing the importance of relationships and spiritual growth.",
        "amazonLink": "https://amzn.to/408Q1dF"
    },
    {
        "title": "The E-Myth Revisited",
        "author": "Michael Gerber",
        "genre": "Business",
        "popularity": 95,
        "khe_favorite": True,
        "synopsis": "Gerber dispels the myths surrounding starting your own business and shows how commonplace assumptions can get in the way of running a business. He walks you through the steps in the life of a business from entrepreneurial infancy, through adolescent growing pains, to the mature entrepreneurial perspective, the guiding light of all businesses that succeed.",
        "amazonLink": "https://amzn.to/3wD4Hp0"
    },
    {
        "title": "Siddhartha",
        "author": "Herman Hesse",
        "genre": "Fiction",
        "popularity": 98,
        "khe_favorite": True,
        "synopsis": "This novel follows the spiritual journey of Siddhartha, a young man in ancient India, as he seeks enlightenment. Through various life experiences and philosophical encounters, Siddhartha learns that true wisdom comes from within and that understanding is achieved through living, not just learning.",
        "amazonLink": "https://amzn.to/3NgjtZk"
    },
    {
        "title": "Tao Te Ching",
        "author": "Lao Tzu",
        "genre": "Philosophy",
        "popularity": 99,
        "khe_favorite": True,
        "synopsis": "This ancient Chinese text presents the philosophy of Taoism through short, poetic verses. It explores themes of harmony, balance, and the natural order of the universe, offering wisdom on how to live in accordance with the Tao, or 'the Way.'",
        "amazonLink": "https://amzn.to/3GLTI2l"
    },
    {
        "title": "True Refuge",
        "author": "Tara Brach",
        "genre": "Spirituality",
        "popularity": 85,
        "khe_favorite": True,
        "synopsis": "Brach offers guidance on finding peace and freedom in the midst of difficulty, stress, and emotional pain. She introduces the RAIN meditation technique and teaches how to tap into our true nature of awareness, compassion, and love as a refuge from life's storms.",
        "amazonLink": "https://amzn.to/41LmIPI"
    },
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "genre": "Spirituality",
        "popularity": 98,
        "khe_favorite": True,
        "synopsis": "Tolle emphasizes the importance of living in the present moment and transcending thoughts of the past or future. He guides readers to discover their true, timeless self beneath the ego and find deep spiritual awakening, leading to personal growth and inner peace.",
        "amazonLink": "https://amzn.to/3n2hctb"
    },
    {
        "title": "Four Thousand Weeks",
        "author": "Oliver Burkeman",
        "genre": "Productivity",
        "popularity": 80,
        "khe_favorite": True,
        "synopsis": "Burkeman challenges conventional productivity wisdom, arguing that time management often increases our sense of busyness and dissatisfaction. He advocates for embracing our limited time on Earth (roughly four thousand weeks) by focusing on what truly matters and accepting our limitations.",
        "amazonLink": "https://amzn.to/39rg1fE"
    }
]

def recommend_book(genre=None):
    if genre:
        genre_books = [book for book in books if book['genre'].lower() == genre.lower()]
        if genre_books:
            return random.choice(genre_books)
        else:
            return None
    else:
        return random.choice(books)

def get_popular_books(n=5):
    return sorted(books, key=lambda x: x['popularity'], reverse=True)[:n]

def get_khe_favorites():
    return [book for book in books if book['khe_favorite']]

def surprise_me():
    weighted_books = []
    for book in books:
        weight = book['popularity'] // 10 + (3 if book['khe_favorite'] else 0)
        weighted_books.extend([book] * weight)
    return random.choice(weighted_books)

def list_genres():
    return list(set(book['genre'] for book in books))

def book_recommender(user_input):
    user_input = user_input.lower()
    
    if 'recommend' in user_input or 'suggest' in user_input:
        for genre in list_genres():
            if genre.lower() in user_input:
                book = recommend_book(genre)
                if book:
                    return f"I recommend '{book['title']}' by {book['author']}. It's a {book['genre']} book with a popularity score of {book['popularity']}.\n\nSynopsis: {book['synopsis']}\n\nYou can find it here: {book['amazonLink']}"
                else:
                    return f"Sorry, I couldn't find a book in the {genre} genre."
        book = recommend_book()
        return f"I recommend '{book['title']}' by {book['author']}. It's a {book['genre']} book with a popularity score of {book['popularity']}.\n\nSynopsis: {book['synopsis']}\n\nYou can find it here: {book['amazonLink']}"
    
    elif 'popular' in user_input:
        popular_books = get_popular_books()
        response = "Here are the 5 most popular books:\n"
        for i, book in enumerate(popular_books, 1):
            response += f"{i}. '{book['title']}' by {book['author']} (Popularity: {book['popularity']})\n"
        return response
    
    elif 'khe' in user_input and 'favorite' in user_input:
        khe_favorites = get_khe_favorites()
        response = "Here are Khe's favorite books:\n"
        for i, book in enumerate(khe_favorites, 1):
            response += f"{i}. '{book['title']}' by {book['author']}\n"
        return response
    
    elif 'surprise' in user_input:
        book = surprise_me()
        return f"Here's a surprise recommendation: '{book['title']}' by {book['author']}. It's a {book['genre']} book with a popularity score of {book['popularity']}.\n\nSynopsis: {book['synopsis']}\n\nYou can find it here: {book['amazonLink']}"
    
    elif 'genre' in user_input:
        genres = list_genres()
        return f"Here are the available genres: {', '.join(genres)}"
    
    else:
        return "I'm not sure what you're asking. You can ask for a recommendation, popular books, Khe's favorites, a surprise recommendation, or list genres."

# Streamlit app
st.title("Book Recommendation Chatbot")

user_input = st.text_input("What kind of book are you looking for?")

if user_input:
    response = book_recommender(user_input)
    st.write(response)

st.write("\nYou can ask for:")
st.write("- A book recommendation (e.g., 'Recommend a business book')")
st.write("- Popular books (e.g., 'What are the most popular books?')")
st.write("- Khe's favorites (e.g., 'Show me Khe's favorite books')")
st.write("- A surprise recommendation (e.g., 'Surprise me')")
st.write("- Available genres (e.g., 'What genres are available?')")
