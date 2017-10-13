 hey_jude = [["Hey", "Jude" , "don't",  "make",  "it",  "bad"],
            ["Take",  "a",  "sad",  "song",  "and", "make",  "it",  "better"],
            ["Remember", "to", "let", "her", "into", "your", "heart"],
            ["Then", "you", "can", "start", "to", "make", "it", "better"],
            ["Hey", "Jude", "don't", "be", "afraid"],
            ["You", "were", "made", "to", "go", "out", "and", "get", "her"],
            ["The", "minute", "you", "let", "her", "under", "your", "skin"],
            ["Then", "you", "begin", "to", "make", "it", "better"],
            ["And", "anytime", "you", "feel", "the", "pain", "hey","Jude", "refrain"],
            ["Don't", "carry", "the", "world", "upon", "your", "shoulders"],
            ["For", "well", "you", "know", "that", "it's", "a", "fool", "who", "plays", "it", "cool"],
            ["By", "making", "his", "world", "a", "little", "colder"],
            ["Hey", "Jude", "don't", "let", "me", "down"],
            ["You", "have", "found", "her", "now", "go", "and", "get", "her"],
            ["Remember", "to", "let", "her", "into", "your", "heart"],
            ["Then", "you", "can", "start", "to", "make", "it", "better"],
            ["So", "let", "it", "out", "and", "let", "it", "in", "hey", "Jude", "begin"],
            ["You're", "waiting", "for", "someone", "to", "perform", "with"],
            ["And", "don't", "you", "know", "that", "it's", "just", "you", "hey", "Jude", "you'll", "do"],
            ["The", "movement", "you", "need", "is", "on", "your", "shoulder"],
            ["Hey", "Jude", "don't", "make", "it", "bad"],
            ["Take", "a", "sad", "song", "and", "make", "it", "better"],
            ["Remember", "to", "let", "her", "under", "your", "skin"],
            ["Then", "you'll", "begin", "to", "make", "it"],
            ["Better", "better", "better", "better", "better", "better", "oh"]]


def coleman_liau_index(text):
      index = 0.0
      wcount = 0.0
      lcount = 0.0
      L = 0.0
      S = 0.0
      for sentences in range(len(hey_jude)):
            for words in range(len(hey_jude[sentences])):
                  lcount += len(hey_jude[sentences][words])
                  wcount += 1
      L = (lcount / wcount) * 100
      S = (len(hey_jude) / wcount) * 100
      index = (0.0588 * L) - (0.296 * S) - 15.8
      print "L = ({} / {}) * 100 => {}".format(lcount, wcount, L)
      print "S = ({} / {}) * 100 => {}".format(len(hey_jude), wcount, S)
      print "CLI = 0.0588L - 0.296S - 15.8 = (0.0588 * {}) - (0.296 * {}) - 15.8 => {}".format(L, S, index)
      return index

hey_jude_cli = coleman_liau_index(hey_jude)

print('The recommended school grade to understand "Hey Jude" lyrics is {}. (Should be between 2 and 3)'.format(hey_jude_cli))

###################################################################################################################################
###################################################################################################################################

text=[["Hey", ",", "Jude"],["don't", "Be", "afraid", ",", "jude"]]
stop_words=["be", ","]

word_dict = {}

for i in range(len(text)):
      for j in range(len(text[i])):
            word_lower = text[i][j].lower()
            if not any(word_lower in word.lower() for word in stop_words):
                  if not any(word_lower in word.lower() for word in word_dict):
                        word_dict[word_lower] = 1
                  else:
                       word_dict[word_lower] += 1

print word_dict

###################################################################################################################################
###################################################################################################################################

hey_jude = [["Hey", "Jude" , "don't",  "make",  "it",  "bad"],
            ["Take",  "a",  "sad",  "song",  "and", "make",  "it",  "better"],
            ["Remember", "to", "let", "her", "into", "your", "heart"],
            ["Then", "you", "can", "start", "to", "make", "it", "better"],
            ["Hey", "Jude", "don't", "be", "afraid"],
            ["You", "were", "made", "to", "go", "out", "and", "get", "her"],
            ["The", "minute", "you", "let", "her", "under", "your", "skin"],
            ["Then", "you", "begin", "to", "make", "it", "better"],
            ["And", "anytime", "you", "feel", "the", "pain", "hey","Jude", "refrain"],
            ["Don't", "carry", "the", "world", "upon", "your", "shoulders"],
            ["For", "well", "you", "know", "that", "it's", "a", "fool", "who", "plays", "it", "cool"],
            ["By", "making", "his", "world", "a", "little", "colder"],
            ["Hey", "Jude", "don't", "let", "me", "down"],
            ["You", "have", "found", "her", "now", "go", "and", "get", "her"],
            ["Remember", "to", "let", "her", "into", "your", "heart"],
            ["Then", "you", "can", "start", "to", "make", "it", "better"],
            ["So", "let", "it", "out", "and", "let", "it", "in", "hey", "Jude", "begin"],
            ["You're", "waiting", "for", "someone", "to", "perform", "with"],
            ["And", "don't", "you", "know", "that", "it's", "just", "you", "hey", "Jude", "you'll", "do"],
            ["The", "movement", "you", "need", "is", "on", "your", "shoulder"],
            ["Hey", "Jude", "don't", "make", "it", "bad"],
            ["Take", "a", "sad", "song", "and", "make", "it", "better"],
            ["Remember", "to", "let", "her", "under", "your", "skin"],
            ["Then", "you'll", "begin", "to", "make", "it"],
            ["Better", "better", "better", "better", "better", "better", "oh"]]

stop_words = ['a', 'to', 'it', 'and', 'his', 'nah', 'the', 'you', 'your', 'her', 'be']

def word_count(text, stop_words):
    word_dict = {}
    # please, write here your code
    for i in range(len(text)):
      for j in range(len(text[i])):
            word_lower = text[i][j].lower()
            if not word_lower in stop_words:
                  if not word_lower in word_dict:
                        word_dict[word_lower] = 1
                  else:
                        word_dict[word_lower] += 1
    return word_dict

wc_hey_jude = word_count(hey_jude , stop_words)

print "Most Frequent Word: {}, Number of Times: {}".format(sorted(wc_hey_jude.items(), key=itemgetter(1))[-1][0], sorted(wc_hey_jude.items(), key=itemgetter(1))[-1][1])

###################################################################################################################################
###################################################################################################################################

word_list = []
w_count = 0

wc_hey_jude = word_count(hey_jude , stop_words)

for key, value in wc_hey_jude.iteritems():
      if value == 1:
            word_list.append(key)
            w_count += 1

print "Which words appear only once in hey_jude?: {}".format(word_list)
print "How many are they?: {}".format(w_count)

###################################################################################################################################
###################################################################################################################################

weight = 0.0

word_counts = {'bad': 1, 'begin': 1, 'start': 2, 'better': 1, 'jude': 1}

word_weights = {'bad':       -1.00,
                'sad':       -0.90,
                'pain':      -0.85,
                'fool':      -0.50,
                'shoulders': -0.40,
                'colder':    -0.30,
                'refrain':   -0.10,
                'under':     -0.10,
                'begin':     +0.10,
                'start':     +0.10,
                'cool':      +0.50,
                'better':    +1.00}

def average_sentiment(word_counts, weights):
    # please, write here your code
    avg_sent = 0.0
    weight = 0.0
    for i in word_counts:
        if i in weights:
            weight += weights[i]*float(word_counts[i])
    avg_sent =  weight / sum(word_counts.values())
    return avg_sent

test_sentiment = average_sentiment({'bad': 1, 'begin': 1, 'start': 2, 'better': 1, 'jude': 1}, word_weights)
print("The average sentiment of this test is {} (should be bwtween 0.05 and 0.06)".format(test_sentiment))

###################################################################################################################################
###################################################################################################################################

hj_avg_sent = average_sentiment(word_count(hey_jude, stop_words), word_weights)

if hj_avg_sent > 0:
    print "Positive: {}".format(hj_avg_sent)
elif hj_avg_sent < 0:
    print "Negative: {}".format(hj_avg_sent)

###################################################################################################################################
###################################################################################################################################

hj_f4_avg_sent = average_sentiment(word_count(hey_jude[-1:-5], stop_words), word_weights)

if hj_f4_avg_sent > 0:
    print "Positive: {}".format(hj_f4_avg_sent)
elif hj_f4_avg_sent < 0:
    print "Negative: {}".format(hj_f4_avg_sent)

###################################################################################################################################
###################################################################################################################################

hj_l5_avg_sent = average_sentiment(word_count(hey_jude[-5:], stop_words), word_weights)

if hj_l5_avg_sent > 0:
    print "Positive: {}".format(hj_l5_avg_sent)
elif hj_l5_avg_sent < 0:
    print "Negative: {}".format(hj_l5_avg_sent)

###################################################################################################################################
###################################################################################################################################

ibov = [60148.26,60720.9,61015.09,62056.47,60108.72,59988.1,60771.79,59647.32,59420.86,57434.37,
        57199.14,56869.02,58042.87,59997.64,59505.17,57630.35,55609.07,56470.59,57542.49,57017.55,
        56584.4,54720.25,54502.97,54573.18,55138.35,54244.03,53326.54,53638.69,55377.15,55934.69,
        55850.13,54477.25,54358.7,55519.24,56382.22,55680.41,55162.14,54404.41,53527.01,51408.54,
        51939.6,50717.97,48435.3,49633.16,51270.4,52392.86,48416.33,49228.92,45908.51,48422.75,
        53055.38,51540.58,49593.17,49842.99,51828.46,50782.99,46028.06,49541.27,49798.65,46145.1,
        44517.32,42100.79,40139.85,38593.54,37080.3,35609.54,40829.13,41569.03,36833.02,36441.72,
        36399.09,39441.08,39043.39,35069.73,33818.49,31481.55,29435.11,33386.65,34845.21,37448.77,
        37256.84,38249.44,40254.8,37785.66,36361.91,36665.11,36776.27,37261.9,34373.99,35993.33,
        35789.1,35717.21,34094.66,33404.55,31250.6,34188.83,34812.86,36469.61,36212.65,36595.87]

ibov_delta = [ibov[x] - ibov[x-1] for x in range(1, len(ibov))]

import numpy

ibov_delta_FH = ibov_delta[:len(ibov_delta)/2]
ibov_delta_LH = ibov_delta[len(ibov_delta)/2:]

if numpy.std(ibov_delta_FH) > numpy.std(ibov_delta_LH):
    print "The FIRST 50 days are more volatile (0-50: {} | 50-100: {})".format(numpy.std(ibov_delta_FH), numpy.std(ibov_delta_LH))
else:
    print "The LAST 50 days are more volatile (0-50: {} | 50-100: {})".format(numpy.std(ibov_delta_FH), numpy.std(ibov_delta_LH))

###################################################################################################################################
###################################################################################################################################

import numpy as np

l_outliers = []
u_outliers = []
l_out_count = 0
u_out_count = 0
IQR = 0.0

Q1 = np.percentile(ibov_delta, np.arange(0, 100, 25))[0]
Q3 = np.percentile(ibov_delta, np.arange(0, 100, 25))[2]

print "Q1 = {} | Q3 = {}".format(Q1, Q3)

IQR = Q3-Q1

print "IQR = Q3-Q1 = {} - {} = {}".format(Q3, Q1, IQR)

l_boundarie = Q1-1.5*IQR
u_boundarie = Q3+1.5*IQR

for i in ibov_delta:
  if i > u_boundarie:
    u_outliers.append(i)
    u_out_count += 1
  elif i < l_boundarie:
    l_outliers.append(i)
    l_out_count += 1

print "IQR = Q3-Q1 = {} - {} = {}".format(Q3, Q1, IQR)
print "lower_boundarie = Q1 - 1.5 * IQR = {} - 1.5 * {} = {}".format(Q1, IQR, l_boundarie)
print "upper_boundarie = Q3 - 1.5 * IQR = {} - 1.5 * {} = {}".format(Q3, IQR, u_boundarie)

if l_out_count == 0 and u_out_count == 0:
  print "There's no outliers."
else:
  if l_out_count > 0:
    print "There's {} lower outliers ({})".format(l_out_count, l_outliers)
  else:
    print "There's {} upper outliers ({})".format(u_out_count, u_outliers)

###################################################################################################################################
###################################################################################################################################

lowest_val = 0.0
biggest_val = 0.0

lowest_val = ibov[0]

for i in range(len(ibov)):
  if ibov[i] < lowest_val:
    lowest_val = ibov[i]

print "{} -> {}".format(lowest_val, ibov.index(lowest_val))

biggest_val = lowest_val

for j in range(ibov.index(lowest_val), len(ibov)):
  if ibov[j] > biggest_val:
    biggest_val = ibov[j]

print "{} -> {}".format(biggest_val, ibov.index(biggest_val))

print "The highest percentual gain would be: {:.2f}%".format((lowest_val / biggest_val) * 100)

###################################################################################################################################
###################################################################################################################################

import numpy as np
sales = np.matrix([[1, 3, 4],
                   [2, 1, 5],
                   [0, 2, 4],
                   [4, 2, 1]])

products = np.matrix([['Bread', 'Cheese', 'Jam']])

customers = np.matrix([['John'], 
                       ['Paul'],
                       ['Ringo'],
                       ['George']])

prices = np.array([1.20, 2.12, 0.99])

sum_mon_sales = sales.sum(axis=0)

jam_sales = sum_mon_sales.flat[3]

print "Sold {} Jams this month.".format(jam_sales)

###################################################################################################################################
###################################################################################################################################

sum_cos_sales = sales.sum(axis=1)

print "Paul bought {} products.".format(sum_cos_sales.flat[2])

###################################################################################################################################
###################################################################################################################################

np.multiply(prices, sales[2])

###################################################################################################################################
###################################################################################################################################

np.multiply(prices, sales).sum(axis=1)

###################################################################################################################################
###################################################################################################################################

print "Total: {:.2f}".format(np.multiply(prices, sales).sum(axis=1).sum())

###################################################################################################################################
###################################################################################################################################

print "Total (+0.1): {:.2f}".format(np.multiply((prices + 0.1), sales).sum(axis=1).sum())


print "Total (+ 0.1 + 20%): {:.2f}".format(np.multiply(((prices + 0.1)*1.2), sales).sum(axis=1).sum())

for p in range(len(products)):
  print "{}: ${:.2f}".format(products.flat[p], (prices[p] + 0.1)*1.2)

for c in range(len(customers)):
  print "{}: {}".format(customers.flat[c], np.multiply((prices + 0.1)*1.2, sales[c]))

