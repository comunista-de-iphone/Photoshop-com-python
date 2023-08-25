import win32com.client
import os
from pathvalidate import sanitize_filename


class Photoshopy:
    app = None  # atributo do photoshop
    psd_file = None  # arquivo aberto do photoshop

    def __init__(self):  # function constructor
        self.app = win32com.client.Dispatch("Photoshop.Application")
        # self.app.Visible = False



    def closePhotoshop(self):
        self.app.Quit()


 # verifica se o arquivo existe, senão fecha o ps
    def openPSD(self, filename):  
        if os.path.isfile(filename) == False:
            self.closePhotoshop()
            return False

        self.app.Open(filename)
        self.psd_file = self.app.Application.ActiveDocument
        return True



    def closePSD(self):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        self.app.Application.ActiveDocument.Close(2)


# atualiza o texto nas camadas
    def updateLayerText(self, Layer_name, text, size):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        layer = self.psd_file.ArtLayers[Layer_name]
        layer_text = layer.TextItem
        layer_text.contents = text
        layer_text.size = size
        return True



    def hideShowLayer(self, Layer_name, ativar):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        layer = self.psd_file.ArtLayers[Layer_name]
        layer.Visible = ativar



    def exportJPEG(self, filename, folder="", quality=100):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)
        filename = sanitize_filename(filename)
        full_path = os.path.join(folder, filename)
        options = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
        options.Format = 6
        options.Quality = quality
        self.psd_file.Export(ExportIn = full_path, ExportAs = 2, Options = options)
        return os.path.isfile(full_path)
