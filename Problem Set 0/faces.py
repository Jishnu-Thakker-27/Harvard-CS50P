def main():
    text=input("Enter the text: ")
    print(convert(text))


def convert(text):
    if text==":)":
        return "🙂"
    elif text==":(":
        return "🙁"
    else: 
        return text 
    
main()