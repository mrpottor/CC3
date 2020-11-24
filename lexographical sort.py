# Python3 implementation to Sort strings 
# according to the frequency of 
# characters in ascending order 

# Returns count of character in the string 
def countFrequency(string , ch) : 

	count = 0; 

	for i in range(len(string)) : 

		# Check for vowel 
		if (string[i] == ch) : 
			count += 1; 

	return count; 

# Function to sort the string 
# according to the frequency 
def sortArr(string) : 
	n = len(string); 

	# Vector to store the frequency of 
	# characters with respective character 
	vp = []; 

	# Inserting frequency 
	# with respective character 
	# in the vector pair 
	for i in range(n) : 

		vp.append((countFrequency(string, string[i]), string[i])); 
		
	# Sort the vector, this will sort the pair 
	# according to the number of characters 
	vp.sort(); 
	
	# Print the sorted vector content 
	for i in range(len(vp)) : 
		print(vp[i][1],end=""); 

# Driver code 
if __name__ == "__main__" : 

	string = "geeksforgeeks"; 

	sortArr(string); 

	# This code is contributed by Yash_R 
