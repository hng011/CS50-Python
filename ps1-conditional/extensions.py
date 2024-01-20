def is_has_suffix(x:str) -> str:
    x=x.lower()
    if "." in x:
        if ("jpeg" in x) or ("jpg" in x): return "image/jpeg"
        elif "gif" in x: return "image/gif"
        elif "png" in x: return "image/png"
        elif "pdf" in x: return "application/pdf"
        elif "txt" in x: return "text/plain"
        elif "zip" in x: return "application/zip"
        else: return is_has_suffix("undefined")
    else:
        return "application/octet-stream"

print(is_has_suffix(input("File Name: ")))