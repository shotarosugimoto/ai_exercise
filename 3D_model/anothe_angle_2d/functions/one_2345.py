from gradio_client import Client


class One2345:

    def __init__(self):
        self.client = Client("https://one-2-3-45-one-2-3-45.hf.space/")
        self.selected_path_list = []
        self.generative_path_list = []

    def initial_process(self, initial_image_path):
        clip_image_path = self.client.predict(
            initial_image_path,
            api_name="/preprocess"
        )
        self.selected_path_list = [clip_image_path]
        return clip_image_path

    def generate_new(self):
        for path in self.selected_path_list:
            result_tuple = self.client.predict(
                path,
                3,
                75,
                fn_index=31
            )
            self.generative_path_list.append(result_tuple[2])
            self.generative_path_list.append(result_tuple[3])
            self.generative_path_list.append(result_tuple[4])
            self.generative_path_list.append(result_tuple[5])
            self.generative_path_list.append(result_tuple[6])
            self.generative_path_list.append(result_tuple[7])
            self.generative_path_list.append(result_tuple[8])
            self.generative_path_list.append(result_tuple[9])

    def add_select(self):
        self.selected_path_list.append(self.generative_path_list[0])
        self.generative_path_list.pop(0)

    def remove_select(self):
        self.selected_path_list.pop(-1)