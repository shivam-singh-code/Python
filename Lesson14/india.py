from random import choice

capital = "New Delhi"

bird = "Peacock"

flower = "Lotus"

song = "vande mataram"

def randomfunfact():
    funfacts = [
        "New Delhi is the capital of India and was officially inaugurated on February 13, 1931.",
        "The famous India Gate in New Delhi is a war memorial dedicated to 70,000 Indian soldiers who died in World War I.",
        "New Delhi was designed by British architects Sir Edwin Lutyens and Sir Herbert Baker in the early 20th century.",
        "The Rashtrapati Bhavan, the official residence of the President of India, has 340 rooms and is one of the largest presidential residences in the world.",
        "New Delhi hosts the largest spice market in Asia, Khari Baoli, which has been operating since the 17th century.",
        "The Lotus Temple in New Delhi is one of the most visited religious sites in the world.",
        "New Delhi has one of the largest metro networks in the world, covering over 390 kilometers.",
        "Delhi’s Akshardham Temple holds the Guinness World Record for being the largest Hindu temple complex in the world.",
        "New Delhi is home to the Parliament of India, which was completed in 1927 and designed in a circular shape.",
        "Connaught Place, one of New Delhi’s busiest shopping and business districts, was modeled after the Royal Crescent in Bath, England."
    ]
    
    index = choice("0123456789")
    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()