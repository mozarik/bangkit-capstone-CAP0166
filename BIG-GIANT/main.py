#For aggregating predict data with url image
def aggregate(data, url_face):
  dicturl = {"url":url_face}
  data[0].update(dicturl)
  dict_with_url = data[0]
  return dict_with_url