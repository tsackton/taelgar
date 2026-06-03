## python program to remove secret text 

import re
import os
import sys

def process_matches(matches, mode, input_str, filename, secret_storage_root):
 
     # Initialize a counter for the match number
    match_num = 0

    # Iterate over the matches
    for match in matches:
        # Extract the contents of the first group in the tuple
        secret = match[0] or match[1] or match[2]

        # Increment the match number
        match_num += 1

        #print(f"Match: %s" % (match,), file=sys.stderr)
        #print("Secret: \n------\n" + secret + "\n----\n", file=sys.stderr)

        if mode == "save":
            # We are saving the secrets

            #print("Saving secrets", file=sys.stderr)
            # Construct the secret storage filename
            secret_storage_filename = os.path.join(secret_storage_root, filename + "." + str(match_num))

            # Write the secret to the secret storage file
            with open(secret_storage_filename, "w") as f:
                f.write(secret)

            # Replace the secret in the input string with the placeholder text
            if (match[2]):
               # print("Got yaml secret", file=sys.stderr)
                input_str = re.sub(re.escape(secret) + r"\#\#secret", "###secret[" + str(match_num) + "]", input_str, flags=re.DOTALL)
            elif (match[0]): 
                input_str = re.sub(r"%%SECRET" + re.escape(secret) + r"%%", "%%SECRET[" + str(match_num) + "]%%", input_str, flags=re.DOTALL)
            else: 
                input_str = re.sub(r"%%SECRET" + re.escape(secret), "%%SECRET[" + str(match_num) + "]%%", input_str, flags=re.DOTALL)

        elif mode == "restore":
            # We are restoring the secrets

            # Construct the secret storage filename
            secret_storage_filename = os.path.join(secret_storage_root, filename + "." + str(match_num))

            # Read the secret from the secret storage file
            with open(secret_storage_filename, "r") as f:
                restored_secret = f.read()

            # Replace the placeholder text in the input string with the secret
            if (match[0] or match[1]): 
                restored_secret = "%%SECRET" + restored_secret + "%%"
                input_str = re.sub(r"%%SECRET\[" + str(match_num) + r"\]%%", restored_secret, input_str, flags=re.DOTALL)
            else:
                restored_secret = restored_secret + "##secret"
                input_str = re.sub(r"\#\#\#secret\[" + str(match_num) + r"\]", restored_secret, input_str, flags=re.DOTALL)

    # Return the modified input string
    return input_str

## sys.argv[1] is save or restore
## sys.argv[2] is file name
## sys.argv[3] is secrets directory

## secret_storage_root has the base path for the secrets direct
secret_storage_root = sys.argv[3]

## filename has the input filename
filename = os.path.basename(sys.argv[2])

# Read the contents of standard input as a string
input_str = sys.stdin.read()

# Use a regular expression to find all substrings that match the pattern "%% ... %%"
# or that start with "%%" and continue to the end of the input string
pattern = r"%%SECRET(.+?)%%|%%SECRET(.+?)\Z|^([^\n\r]+)\#\#secret.*?$"
matches = re.findall(pattern, input_str, flags=re.MULTILINE|re.DOTALL)

# Check if there are any matches
if matches:
    # Call the process_matches function on the list of matches
    input_str = process_matches(matches,sys.argv[1], input_str, filename, secret_storage_root)

print(input_str, end="")
