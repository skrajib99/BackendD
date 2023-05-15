# import sys

# print(sys.path)

# import pandas as pd
# from wordcloud import WordCloud

from flask import Flask,render_template,request,render_template_string,redirect,url_for
from preprocess import preprocess
import helper as hp
import matplotlib.pyplot as plt
import io
import base64
import subprocess
# import psutil


app = Flask(__name__)

@app.route('/')
def home():
    # return 'Hello, World!'
    return render_template("index.html")

# @app.route('/upload', methods=['POST'])
# def upload():

#     # Redirect to the Streamlit app URL
#     # return redirect('http://localhost:8501')
#     subprocess.Popen(['streamlit', 'run', 'result.py'])

#     return 'REDIRECTING'
#     # return render_template('index.html')




# @app.route('/upload', methods=['POST'])
# def upload_file():
#     uploaded_file = request.files['file']
#     if uploaded_file.filename.endswith('.txt'):
#         filename = uploaded_file.filename
#         uploaded_file.save(filename)
#         # return 'File uploaded successfully'
#         with open(filename,'r',encoding='utf-8') as f:
#             file_contents = f.read()
#         df = preprocess(file_contents)

#         #Top Statistics
#         num_message,len_of_total_words, media_message, links= hp.fetch_stats('Overall',df)

#         #Most Busiest user:

#         x,new_df = hp.most_busy_users(df)
#         fig,ax = plt.subplots(figsize =(12, 7))
#         # plt.bar(x.index,x.values,color='red')
#         ax.bar(x.index,x.values,color='red')
#         # plt.xticks(rotation = 'vertical')

#         # # Convert the graph to base64-encoded PNG image
#         buffer = io.BytesIO()
#         plt.savefig(buffer, format='png')
#         buffer.seek(0)
#         image_data = base64.b64encode(buffer.getvalue()).decode()

#         # image_data = fig.savefig('bar_graph.png')


#         ####Wordcloud
#         df_wc = hp.create_wordcoud('Overall',df)
#         fig,ax = plt.subplots()
#         ax.imshow(df_wc)

#         buffer2 = io.BytesIO()
#         plt.savefig(buffer2, format='png')
#         buffer2.seek(0)
#         word_Cloud = base64.b64encode(buffer2.getvalue()).decode()


#         ####most common words
#         most_common_words_df = hp.most_common_words("Overall",df)
#         fig,ax = plt.subplots(figsize =(10, 7))
#         ax.bar(most_common_words_df[0],most_common_words_df[1],color='green')
#         plt.xticks(rotation='vertical')

#         buffer3 = io.BytesIO()
#         plt.savefig(buffer3, format='png')
#         buffer3.seek(0)
#         most_common_words= base64.b64encode(buffer3.getvalue()).decode()


#         #####emoji Analysis

#         emoji_df = hp.emoji_helper('Overall',df)
#         fig = plt.figure(figsize =(10, 7))
#         plt.pie(emoji_df[1].head(10), labels = emoji_df[0].head(10),autopct="%0.2f")


#         buffer4 = io.BytesIO()
#         plt.savefig(buffer4, format='png')
#         buffer4.seek(0)
#         emoji_analysis= base64.b64encode(buffer4.getvalue()).decode()


#         #####timeline monthly

#         timeline = hp.monthly_timeline("Overall",df)
#         fig,ax = plt.subplots(figsize =(10, 10))
#         ax.plot(timeline['time'],timeline['message'],color='green')
#         plt.xticks(rotation='vertical')

#         buffer5 = io.BytesIO()
#         plt.savefig(buffer5, format='png')
#         buffer5.seek(0)
#         monthly_timeline= base64.b64encode(buffer5.getvalue()).decode()

#         #####timeline daily

#         daily_timeline = hp.daily_timeline("Overall",df)
#         fig,ax = plt.subplots(figsize =(10, 10))
#         ax.plot(daily_timeline['only_date'],daily_timeline['message'],color='green')
#         plt.xticks(rotation='vertical')

#         buffer6 = io.BytesIO()
#         plt.savefig(buffer6, format='png')
#         buffer6.seek(0)
#         daily_timeline= base64.b64encode(buffer6.getvalue()).decode()


#         busy_day = hp.week_activity_map("Overall",df)
#         fig,ax = plt.subplots(figsize =(7, 8))
#         ax.bar(busy_day.index,busy_day.values)
#         plt.xticks(rotation='vertical')

#         buffer7 = io.BytesIO()
#         plt.savefig(buffer7, format='png')
#         buffer7.seek(0)
#         most_busy_day= base64.b64encode(buffer7.getvalue()).decode()


#         busy_month = hp.month_activity_map("Overall",df)
#         fig,ax = plt.subplots(figsize =(7, 8))
#         ax.bar(busy_month.index,busy_month.values,color='orange')
#         plt.xticks(rotation='vertical')

#         buffer8 = io.BytesIO()
#         plt.savefig(buffer8, format='png')
#         buffer8.seek(0)
#         most_busy_month= base64.b64encode(buffer8.getvalue()).decode()




#         return render_template("result.html",filename=filename,
#                                file_contents= file_contents,df = df,
#                                num_message=num_message,
#                                len_of_total_words=len_of_total_words,
#                                media_message=media_message,
#                                links=links,
#                                fig=image_data, new_df=new_df,
#                                word_Cloud=word_Cloud,
#                                most_common_words=most_common_words,
#                                emoji_df=emoji_df,
#                                emoji_analysis=emoji_analysis,
#                                monthly_timeline=monthly_timeline,
#                                daily_timeline=daily_timeline,
#                                most_busy_day=most_busy_day,
#                                most_busy_month=most_busy_month
#                                )
#     else:
#         return 'Only .txt files are allowed'


@app.route('/aboutUs')
def about():
    return render_template("aboutUs.html")


@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.route('/howTo')
def howTo():
    return render_template("howTo.html")


@app.route('/contactUs')
def contact():
    return render_template("contactUs.html")


if __name__=='__main__':
    app.run(debug=True)