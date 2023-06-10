import os
from PIL import Image


class ImageOptimizer:
    def __init__(self, instance, choice_quality):
        self.instance = instance
        self.quality = choice_quality

    def resize_img(self) -> Image.Image:
        image_path = self.instance.icon.path
        image = Image.open(image_path)

        new_size = (int(image.width * self.quality), int(image.height * self.quality))
        resized_image = image.resize(new_size)

        return resized_image

    def generate_resized_image_filename(self, instance_id):
        return f"img/{self.quality}_resized_{instance_id}.jpg"

    def save_resized_image(self, resized_image):
        image_path = self.instance.icon.path

        resized_image_path = os.path.join(os.path.dirname(image_path),f"{self.quality}_resized_{self.instance.id}.jpg")
        resized_image.save(resized_image_path)

        name_file = self.generate_resized_image_filename(self.instance.id)

        if self.quality == 0.75:
            self.instance.icon_75 = name_file
        elif self.quality == 0.50:
            self.instance.icon_50 = name_file
        elif self.quality == 0.25:
            self.instance.icon_25 = name_file

        self.instance.save()




