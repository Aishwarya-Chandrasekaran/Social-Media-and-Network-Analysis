# ANALYZING THE CHALLENGES ENCOUNTERED BY INTERNATIONAL STUDENTS VIA SOCIAL MEDIA ENGAGEMENT

INTRODUCTION
Nowadays, social media platforms have transformed the way international students engage in academic experiences, providing a unique space for them to connect with prefers from their home countries and around the world. These platforms offer international students a virtual community where they can share their experiences, seek advice, and build meaningful connections. These platforms have become invaluable sources of support and information for international students, who often face unique challenges when studying in foreign countries. Sentiment analysis, topic modelling, and network analysis are powerful tools that can be used to gain a deeper understanding of the social networks of international students on social media. Sentiment analysis can be used to identify the sentiment of the data, such as whether it is positive, negative, or neutral. Topic modelling can be used to identify the main topics that are being discussed in the data. Network analysis can be used to study the relationships between individuals or groups in the data. By combining these three methods, we can gain a more comprehensive understanding of the social networks of international students, including their communication patterns, interests, concerns, and the role that social media plays in their lives.

The objectives of this report are to:
1.
To examine the tone of conversations among international students on websites like Reddit and YouTube is the first objective. To do this, sentiment analysis methods must be used to ascertain the emotional undertone of their interactions. The objective is to identify the underlying emotions, whether they are pleasant, negative, or neutral, as well as potentially more complex feelings like elation, annoyance, or contentment. The emotional climate of these online communities can be better understood with the aid of sentiment analysis.
2.
In order to determine the common themes and topics of conversation within these online groups, topic modeling approaches will be used for the second purpose. Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF), two topic modeling techniques, can be used to identify the primary subjects and subtopics that overseas students are interested in or conversing about. It might offer a more methodical and data-driven way to comprehend the details of their relationships.
3.
In order to comprehend the organization and connections within the social networks of international students, objective three focuses on network analysis. Building a network graph with people as nodes and their interactions (comments,
4
likes, responses, etc.) as edges can be one way to do this. Key communication
patterns, such as who communicates with whom and how information moves throughout the group, can be uncovered using network analysis. It can also be used to find key players in the network or other influential nodes, such as those with plenty of connections.
4.
The fourth objective looks at how sentiment, subjects, and network structures interact and shape the experiences and interactions of international students on social media platforms in order to provide a comprehensive understanding. It can reveal, for instance, if certain themes are linked to particular sentiment patterns or whether people who express a certain mood prefer to develop particular network structures. The dynamics of these online communities may be better understood with the help of an all-encompassing methodology.

DATA COLLECTION
Data collection plays a vital role in the whole process. The data collected for each platform is as follows:
Reddit
The process begins with data collection from the "internationalStudents" subreddit on Reddit. A Python script utilizing the Python Reddit API Wrapper (PRAW) is employed for this purpose. Around 1000 submissions extracted with attributes.

YouTube:
The dataset is structured as a JSON object , with each element representing a YouTube video and its associated comments and replies . The maximum number of video data to be fetched per keyword and is defined (in this case , it's set to 25 due to YouTube API daily quota , but can be adjusted ). The data is retrieved based on certain keywords . 
The information for each post and its comments is then stored in a JSON format in a file named "i ‘internationalStudentsyouTube.json
