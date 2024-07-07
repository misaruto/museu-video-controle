import segno

def generate_qrcode(content:str,output_image:str,border=1,scale=5):
  qrcode = segno.make(content)
  qrcode.save(output_image, border=border,scale=scale)