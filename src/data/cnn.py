import torch
import torchvision as vision
import torchxrayvision as xrv
import skimage.io as io


class XRayDeepVision:
    def __init__(self, resize=False, error=0.7) -> None:
        if resize:
            self.__transform = vision.transforms.Compose([
                xrv.datasets.XRayCenterCrop()
            ])
        else:
            self.__transform = vision.transforms.Compose([
                xrv.datasets.XRayCenterCrop(),
                xrv.datasets.XRayResizer(224)
            ])
        self.__model = xrv.models.get_model('densenet121-res224-all')
        self.__error = error
        self.output = None
        self.image = None

    def load_image(self, file) -> None:
        img = io.imread(file)

        if len(img.shape) > 2:
            img = img[:, :, 0]

        img = img[None, :, :]
        img = xrv.datasets.normalize(img, 255)
        self.image = self.__transform(img)

    def run(self) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
        with torch.no_grad():
            self.image = torch.from_numpy(self.image).unsqueeze(0)
            preds = self.__model(self.image).cpu()
            self.output = list(zip(
                xrv.datasets.default_pathologies,
                preds[0].detach().numpy()
            ))
            return (
                self.output, 
                list(filter(lambda x: x[1] >= self.__error, self.output))
            )
