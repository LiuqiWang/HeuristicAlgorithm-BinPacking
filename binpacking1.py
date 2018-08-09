# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 00:52:02 2018

@author: liuqi
"""

def binpack(articles,bin_cap):
        
    my_team_number_or_name = "lwang19"    # always return this variable as the first item
    bin_contents = []    # use this list document the article ids for the contents of 
                         # each bin, the contents of each is to be listed in a sub-list
    

    # map articles dictionary to list of lists 
    item_list = [[k,v] for k,v in articles.items()]
    item_list1 = [[k,v] for k,v in articles.items()]
    # sort articles by volume large to small 
    j = lambda x:x[1]
    item_list.sort(key=j,reverse=True)
    item_list1.sort(key=j)
    item_keys = [item[0] for item in item_list]
    item_keys1 = [item[0] for item in item_list]

    pack = [] #keep record of items in the current bin 
    load = 0.0 #the current volumn
    for i in range(len(item_keys)):
        if item_keys[i] != item_keys1[i]:
            if load <= bin_cap:
                pack_item = item_keys[i]
                load += articles[pack_item]
                if load <= bin_cap:
                    pack.append(pack_item)
                    #now try from the other source
                    pack_item = item_keys1[i]
                    load += articles[pack_item]
                    if load <= bin_cap:
                        pack.append(pack_item)
                elif load > bin_cap:
                    bin_contents.append(pack)
                    pack=[]
                    load = 0.0
                    pack_item = item_keys[i]
                    load += articles[pack_item]
                    pack_item = item_keys1[i]
                    load += articles[pack_item]
            if i==len(item_keys)-1:
                bin_contents.append(pack)
        if item_keys[i] == item_keys1[i]:
            if load <= bin_cap:
                pack_item = item_keys[i]
                load += articles[pack_item]
                if load <= bin_cap:
                    pack.append(pack_item)
                elif load > bin_cap:
                    bin_contents.append(pack)
                    pack=[]
                    load = 0.0
                    pack_item = item_keys[i]
                    load += articles[pack_item]
                    pack.append(pack_item)
            if i==len(item_keys)-1:
                bin_contents.append(pack)
        
            
    return my_team_number_or_name, bin_contents       # use this return statement when you have items to load in the knapsack
