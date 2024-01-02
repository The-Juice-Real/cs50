def main():
    name = input("What's your filename? ").strip().lower()
    print(nametomedia(name))

def nametomedia(i):
    #if there's a "." in the text
    if i.find(".") != -1:
        ext = i.rsplit(".")[-1]
        match ext:
            case "gif" | "png" | "jpeg":
                return f"image/{ext}"
            case "jpg":
                return "image/jpeg"
            case "pdf" | "zip":
                return f"application/{ext}"
            case "txt":
                return "text/plain"
            case _:
                return "application/octet-stream"
    #if there's no "."
    else:
        return "application/octet-stream"

main()

