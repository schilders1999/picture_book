import os
import configparser
import sys
import webbrowser
import urllib.request
import openai
import numpy as np

pageNames = []

class Dalle:
        
        def __init__(self, img_sz="512", n_images=1):
                self._api_keys_location = "./config"
                path = os.path.join(os.getcwd(), 'static', 'images', dirName.replace(" ", ""))
                self._generated_image_location = path
                self._page_contents = pageContents
                self._stream = True
                self._img_sz = img_sz
                self._n_images = n_images
                self._image_urls = []
                self._input_prompt = None
                self._response = None
                self.initialize_openai_api()

        def create_template_ini_file(self):
                """
                If the ini file does not exist create it and add the organization_id and
                secret_key
                """
                if not os.path.isfile(self._api_keys_location):
                        with open(self._api_keys_location, 'w') as f:
                                f.write('[openai]\n')
                                f.write('organization_id=\n')
                                f.write('secret_key=\n')

                        print('OpenAI API config file created at {}'.format(self._api_keys_location))
                        print('Please edit it and add your organization ID and secret key')
                        print('If you do not yet have an organization ID and secret key, you\n'
                                'need to register for OpenAI Codex: \n'
                                'https://openai.com/blog/openai-codex/')
                        sys.exit(1)


        def initialize_openai_api(self):
                """
                Initialize the OpenAI API
                """
                # Check if file at API_KEYS_LOCATION exists
                self.create_template_ini_file()
                config = configparser.ConfigParser()
                config.read(self._api_keys_location)

                openai.organization_id = config['openai']['organization_id'].strip('"').strip("'")
                openai.api_key = config['openai']['secret_key'].strip('"').strip("'")
                del config

        def read_from_command_line(self, pageText):
                self._input_prompt = "Draw a picture for the sentence: " + pageText + ". Also, keep the following prompt in mind: " + dirName + ". Draw in a picture book style without including any generated text."
                

        def generate_image_from_prompt(self):
                self._response = openai.Image.create(
                        prompt=self._input_prompt,
                        n=self._n_images,
                        size=f"{self._img_sz}x{self._img_sz}",
                )
                
        def get_urls_from_response(self):
                for i in range(self._n_images):
                        self._image_urls.append(self._response['data'][i]['url'])

        def open_urls_in_browser(self, image_urls=None):
                if image_urls is None:
                        image_urls = self._image_urls
                for url in image_urls:
                        webbrowser.open(url)

        def save_urls_as_image(self):
                if not os.path.isdir(self._generated_image_location):
                        os.mkdir(self._generated_image_location)
                for idx, image_url in enumerate(self._image_urls):
                        file_name = f"{self._generated_image_location}/{str(counter)}.png"
                        urllib.request.urlretrieve(image_url, file_name)
                        pageNames.append(file_name)
                        print(f"Generated image stored in: {file_name}")
        
        def generate_and_save_images(self, pageText):
                self.read_from_command_line(pageText)
                self.generate_image_from_prompt()
                self.get_urls_from_response()
                self.save_urls_as_image()



def begin(arrayValue, input_string):
        global dirName
        dirName = input_string
        global counter
        counter = 1
        global pageContents

        for x in arrayValue:
                pageContents = arrayValue
                commandLineDalle = Dalle()
                commandLineDalle.generate_and_save_images(x)
                commandLineDalle.open_urls_in_browser()
                counter = counter +1

        