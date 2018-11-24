#!/usr/bin/env python
#

import pandas as pd
import wisepy.nn as nn
import utils.logging as logging
from utils import load_json, mkdir
import wisepy.nn.transform as transform
import os
def build_convolution(**args):
	
	ModelTemplate = args.get("template",None)

	template_functions = {
	"relu_softmax": nn.CNN.relu_softmax
	}
	if ModelTemplate and ModelTemplate in template_functions:
		NetArgs = args["netargs"]
		NNS = tuple(NetArgs.get("nns",[16,32,64]))
		InSize = NetArgs.get("in_s",(465,310))
		OutSize = NetArgs.get("out_s",8)

		#<-
		logging.info("Building a template convolution model \
			(%s) with:\ninput size: \
			(%d %d %d)\noutput size \
			%d" % (ModelTemplate,InSize[0],InSize[1],InSize[2],OutSize))
		#->

		model = template_functions[ModelTemplate](NNS,InSize,OutSize)

	return model
def build_sequential(**args):
	ArchitectureFile	= args["Architecture"]
	netArch = load_json(ArchitectureFile)

	if netArch["structure"] == "conv":

		#<-
		logging.info("Training a convolution model")
		#->

		return build_convolution(**netArch)

ModelFunctions = {
	"sequential": build_sequential
}

class ImageClassifier:
	def __init__(self,classifier_path=None):
		self._model = None
		if classifier_path:
			self.load_model(classifier_path)
	def load_model(self,path):
		self._model = nn.load_network(path)
	def test(self,dataset):
		return self._model.test(dataset)
	def predict_dataset(self,dataset):
		predictions = [self._model.predict(i) for i in dataset]
	def predict(self,instance):
		return self._model.predict(instance)
	def info(self):
		return self._model.info
	def labels(self):
		return self._model.labels
	def transformer(self):
		return self._model.itransformer
	def train(self,**args):
		ModelType		= args["ModelType"]
		Dataset 		= args["Dataset"]
		NamingProtocol 	= args["NamingProtocol"]
		ImageSize 		= tuple(args["ImageSize"])
		#ModelID			= args.get("ModelID",None)
		Epochs 			= args.get("Epochs",50)
		BatchSize 		= args.get("BatchSize",20)
		CheckPoint 		= args.get("CheckPoint",None)
		ITransformer	= args.get("ITransformer",None)
		Labels			= args.get("Labels",None)

		model = ModelFunctions[ModelType](**args)

		#<-
		logging.info("Start training...")
		#->

		model.train(Dataset,NamingProtocol,epochs=Epochs,
			batch_size=BatchSize,img_size=ImageSize,checkpoint=CheckPoint)

		#<-
		logging.info("Finished training...")
		#->

		# if ModelID:
		# 	TrainedModels[ModelID] = model
		# else:
		# 	TrainedModels[utl.random_text(5)] = model

		if ITransformer:
			with open(ITransformer) as f:
				transText = f.read()
			model.set_itransformer(transform.load(transText))
		
		if Labels:
			with open(Labels) as f:
				labels = f.read().split("\n") 
			
			model.set_labels(labels)

		self._model = model
	def test(self,**args):
		Dataset 		= args["Dataset"]
		NamingProtocol 	= args["NamingProtocol"]
		
		info = self.info()

		#<-
		logging.info("Start testing...")
		#->

		result = self._model.test(Dataset,ds_mode=NamingProtocol,
			img_size=info["ImageSize"])

		#<-
		logging.info("Finished testing...")
		#->

		return result

	def publish(self,prefix):

		if os.path.exists("%s" % prefix):
			logging.warn("Model couldn't be saved because %s.json already exists!!" % prefix)
			return
		mkdir(prefix)
		self._model.save("%s/%s" % (prefix,prefix.split("/")[-1]))
def get_param():
	"""
	handle command line parameters, test using -h parameter....
	"""
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-t','--traintest',help='train or test',default='train')
	parser.add_argument('-d','--data',help='path to dataset',default=None)
	parser.add_argument('-s','--imagesize',help='training image size',default=[314,420])
	parser.add_argument('-e','--epochs',help='number of epochs for the training',default=50)
	parser.add_argument('-b','--batchsize',help='batch size for the training',default=20)
	parser.add_argument('-a','--architecture', help='network architecture file',default=None)
	parser.add_argument('-p','--prefix',
		help='model prefix (loading for testing, saving for training)',default=None)
	parser.add_argument('-l','--labels',help='file name for actual labels\' names',default=None)
	parser.add_argument('-r','--transformer', help='input transformer file', default=None)
	args = parser.parse_args()
	
	if type(args.imagesize) == str:
		args.imagesize = [int(i) for i in args.imagesize.split(",")]
	if type(args.epochs) == str:
		args.epochs = int(args.epochs)
	if type(args.batchsize) == str:
		args.batchsize = int(args.batchsize)
			
	return args.traintest,args.architecture,args.data,args.imagesize, \
		   args.epochs,args.batchsize,args.prefix,args.labels,args.transformer
def main():

	traintest,architecture,data,imagesize,epochs,batchsize,prefix,labels,transformer = get_param()
	

	if traintest == "train":
		trainArg = {
			"ModelType":"sequential",
			"Dataset": data,
			"ImageSize": imagesize,
			"Epochs": epochs,
			"BatchSize": batchsize,
			"Labels": labels,
			"Architecture": architecture,
			"NamingProtocol": "scikit",
			"ITransformer": transformer
		}
		clsf = ImageClassifier()
		clsf.train(**trainArg)
		clsf.publish(prefix)
	if traintest == "test":
		testArg = {
			"Dataset": data,
			"NamingProtocol": "scikit"
		}
		clsf = ImageClassifier(prefix)
		results = clsf.test(**testArg)
		print(results)

if __name__ == '__main__':
	main()