sample_url = 'https://wsp.kbtu.kz'
# sample[start:end:step]
# print sample URL
# print reversed URL
# print top level domain (.kz)
# print URL without https://
# print URL without https:// and top level domain
# 1
start=1
end=len(sample_url)
print(sample_url[start:end:2])
# 2
print(sample_url)
# 3
print(sample_url[::-1])
# 4
print(sample_url[:end-3])
# 5
print(sample_url.replace("https://",""))
# 6
print(sample_url[8:end-3])