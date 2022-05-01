#!/usr/bin/env python3
''' HOW TO ADD TO A LIST '''
dict_1 = {
            'key_a' : ['item_a', 'item_b', 'item_c'],
            'key_b' : ['item_d', 'item_e', 'item_f']
         }
dict_2 = {  
            'key_c' : ['item_g', 'item_h', 'item_i'],
            'key_d' : ['item_j', 'item_k', 'item_l']
         }

def main():
    while True:
        print(f"dict_1 is:\n {dict_1}\n\n dict_2 is:\n {dict_2}\n")
        print(f"dict_1['key_a'] is:\n {dict_1['key_a']}\n\n")
        
        key = input("Choose a key (key_a through key_d): ")
        source = input("Choose a source (dict_1 or dict_2): ")
        dest = input("Choose a destination (dict_1 or dict_2):")
        
        print(f"\n\nKEY: {type(key)} -- {str(f'{key}')} -- {key}")
        print(f"KEY: {type(source)} -- {str(f'{source}')} -- {source}")
        print(f"KEY: {type(dest)} -- {str(f'{dest}')} -- {dest}\n\n")
                
        #if key in source:                                                      # FAILS - source is treated as its string, not the matching dict
        if key in dict_1 and source != dest:                                    # ITERNATES THE LIST AND THEN APPENDS
            source_length = len(dict_1[key])
            print(f"Source length: {source_length}")
            key_list = []
            for i in range(source_length):
                print(f"Range iteration: {i}")
                key_list.append(dict_1[key][i])
            dict_2[key] = key_list
            dict_1.pop(key)
        
        if key in dict_2 and source != dest:                                    # DIRECT TRANSFER METHOD
            dict_1[key] = dict_2[key]
            dict_1.pop(key)
                         
        print(f"=== NEW VALUES ===\n\n dict_1 is:\n {dict_1}\n dict_2 is:\n {dict_2}\n\n")                   
        break

if __name__ == "__main__":
    main()