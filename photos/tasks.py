import boto3
import os
from pathlib import Path
from botocore.exceptions import ClientError
from PIL import Image
#from exif import Image
from PIL.ExifTags import TAGS
import piexif

def sync_photos():
    s3 = boto3.resource('s3', aws_access_key_id='AKIA3EMLCJPMYDZZZF3M', aws_secret_access_key='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')
    s3_client = boto3.client('s3', aws_access_key_id='AKIA3EMLCJPMYDZZZF3M', aws_secret_access_key='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')
    bucket = s3.Bucket('abelaeobigode')

    #entries = os.listdir('/code/Fotos Dani/')
    path = '/code/Fotos Dani/'
    thumb_path = '/code/thumb/'
    entries = Path(path)

    size = 256, 256

    photos = bucket.objects.all()

    for entry in entries.iterdir():
        print(' ')
        print(entry)
        if entry.is_file():
            exists = find_photo(photo = entry.name, photos = photos)
            print(entry.name, exists)
            if not exists:
                uploaded = upload_photo(photo = path + entry.name, s3_client = s3_client, destination = "casamento/" + entry.name)
                print(entry.name, "uploaded", uploaded)

            print(' ')
            exif_dict = piexif.load(path + entry.name)
            #print(exif_dict)
            for ifd in ("0th", "Exif", "GPS", "1st"):
                for tag in exif_dict[ifd]:
                    if ("DateTimeOriginal" == piexif.TAGS[ifd][tag]["name"]):
                        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])
            print(' ')

            thumb = f"thumb/{entry.name}"
            thumb_exists = find_photo(photo = thumb, photos = photos)
            if not thumb_exists:
                print(thumb, thumb_exists)
                with Image.open(path + entry.name) as im:
                    im.thumbnail(size)
                    thumb_filename = f"{thumb_path}/{entry.name}"
                    print('salvar em ', thumb_filename)
                    im.save(thumb_filename, "JPEG")
                    uploaded = upload_photo(photo = thumb_filename, s3_client = s3_client, destination = "thumb/" + entry.name)
                    print(entry.name, "uploaded", uploaded)
            print(' ')

    print('---------------')

def find_photo(photo, photos):
    for item in photos:
        if str(photo) in str(item):
            return True
    return False
        
def upload_photo(photo, s3_client, destination):
    try:
        response = s3_client.upload_file(str(photo), 'abelaeobigode', destination, ExtraArgs={'ACL': 'public-read'})
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    return True