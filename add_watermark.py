from PIL import Image, ImageDraw, ImageFont


def start_process(logo_file, source_file):
    # Opening Image
    img = Image.open(source_file)
    logo = Image.open(logo_file)
    logo2 = logo.copy()
    logo2.putalpha(80)
    logo.paste(logo2, logo)

    # Image Size
    img_w, img_h = img.size
    logo_w, logo_h = logo.size

    # Logo Size ( check longer size, adjust up tp 30% of base image)
    if img_h > img_w:
        logo_h2 = int(img_h * 0.2)
        ratio = logo_h2 / logo_h
        logo_w2 = int(logo_w * ratio)
    else:
        logo_w2 = int(img_w * 0.2)
        ratio = logo_w2 / logo_w
        logo_h2 = int(logo_h * ratio)

    # Resize logo to 20%
    logo = logo.resize((logo_w2, logo_h2))

    # Set logo position
    offset = ((img_w - logo_w2) // 2, (img_h - logo_h2) // 2)

    # Images overlap, show and save
    watermark = img.copy()
    watermark.paste(logo,offset,logo)
    return watermark
    # watermark.save(r'watermark.jpg')