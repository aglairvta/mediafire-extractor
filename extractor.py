import re

def extract_codes_from_link(shared_link):
    try:
        match = re.search(r'/folder/([^/]+)/', shared_link)
        if match:
            codigos = match.group(1).split(',')
            return codigos
        else:
            print("Formato do link não reconhecido.")
            return []
    except Exception as e:
        print(f"Erro ao extrair códigos do link: {e}")
        return []

def generate_urls(codigos):
    urls = []
    for codigo in codigos:
        url = f"https://www.mediafire.com/file/{codigo}/"
        urls.append(url)
    return urls

shared_link = input("Cole o link compartilhado do MediaFire: ").strip()

codigos = extract_codes_from_link(shared_link)

if codigos:

    urls = generate_urls(codigos)
    
    with open("urls.txt", "w") as file:
        for url in urls:
            file.write(url + "\n")
    
    print(f"URLs geradas e salvas em urls.txt.")
else:
    print("Não foram encontrados códigos válidos do MediaFire no link compartilhado.")
