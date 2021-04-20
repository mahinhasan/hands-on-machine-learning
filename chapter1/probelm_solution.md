# Chapter 1 problem solution 

### 1. **How would you define machine learning ?**

 - Machine learning is learning where machine can learn from data and solve spacific problem.

    - Finding, extracting and summarizing relevant data
    - Making predictions based on the analysis data
    - Calculating probabilities for specific results
    - Adapting to certain developments autonomously
    - Optimizing processes based on recognized patterns


### 2 .**Can you name four types of problems where it shines?**

***Answer :***  Machine learning is great for problems whose solution requires a great deal of work or a long list of rules, complex problems that are hard to get a solution of using a traditional method, fluctuating environments and getting insights about complex problems and large data


### 3. **What is a labeled training set?**

***Answer:*** Labeled data is a group of samples that have been tagged with one or more labels. Labeling typically takes a set of unlabeled data and augments each piece of it with informative tags

### 4. **What are the two most common supervised tasks?**
***Answer :*** 

Two Supervised task is -: 

* Classification 
* Regression 

### 5. **Can you name four common unsupervised tasks?**

***Answer:***

* Four common unsupervised tasks is below:
- clustering, 
- visualization,
- dimensionality reduction ,
- association rule learning.


### 6. **What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?**

***Answer:***

Reinforcement learning learning would certainly be a viable approach. There have been some papers coming out of the Stanford research group by distinguished researchers such as Andrew Ng on this very topic. Using reinforcement learning, the robot would gradually learn how to walk through different terrains in much the same way as animals learn, by getting rewards and punishments.


### 7. **What type of algorithm would you use to segment your customers into multiple groups?**

***Ansewer:***

* k-means clustering


### 8. **Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?**

***Answer:***
The best algorithm to segment customers into multiple groups is either supervised learning (if the groups have known labels) or unsupervised learning (if there are no group labels).


### 9. **What is an online learning system?***
***Answer:***

In computer science, online machine learning is a method of machine learning in which data becomes available in a sequential order and is used to update the best predictor for future data at each step, as opposed to batch learning techniques which generate the best predictor by learning on the entire training data set

### 10. **What is out-of-core learning?**

***Answer:***
Out-of-core learning refers to a set of algorithms working with data that cannot fit into the memory of a single computer, but that can easily fit into some data storage such as a local hard disk or web repository.

Out of core learning is working on data that is too big to fit on **RAM**. Keras has a built in system for out of core learning that just streams data from the folders you designate. I do not have in-depth knowledge about subject matter however I’ve been using out of core learning in convolutionary neural networks. You can also implement out of core learning in scikit-learn with partial_fit method. You can read about the subject matter from Scikit-Learn’s own documentation from online.

### 11. **What type of learning algorithm relies on a similarity measure to make predictions?**

***Answer:***

**Instance Based Learning:**
Instance-based learning algorithms use a measure of similarity to generalize to new cases. In an instance-based learning system, the algorithm learns the examples by heart, then uses the similarity measure to generalize


### 15. **If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name 3 possible solutions?**
***Answer:***
This is a case where the model is overfitting the training data. To couteract overfitting, we can reduce the complexity of the model by removing features or constraining the parameters. We could gather more data. Finally we can reduce noisiness in the data by fixing errors and removing outliers.


### 18.**What can go wrong if you tune hyperparameters using the test set?**
***Answer:***
- model will not be generalizable to new examples.