import deeplake

try:
    ds = deeplake.load('hub://activeloop/flickr30k')
    dataloader = ds.pytorch(num_workers=0, batch_size=4, shuffle=False)
    print("Flickr30K Ready For Processing")

except:
    print("Loading Failed")
