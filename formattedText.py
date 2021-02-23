import re

def formatRawText(rawText, maxWidth):
    '''
        formatRawText function takes two arguments
        rawText  -> rawtext is the text we want to re-format
        maxWidth -> Max width is the maximum number of characters per line we want to format

        return formattedText -> function returns the formatted text by preserving the exsiting indentation of each section and sub sections
    '''
    lines = rawText.split("\n")
    formattedText = ""

    for line in lines:
        formattedLine = ""
        indent = ""

        # regular expression to get the indentation of existing section and capture the indented string length
        matchingPattern = re.search(r'(^\s+[\d.-]*?\s*)[a-z\[].*', line, re.I)
        if matchingPattern:
            indent = " " * len(matchingPattern.group(1))

        if len(line) > maxWidth:
            words = line.split(" ")
            for word in words:
                # if loop determines the re-formatted text is with in the max width
                # if re-formatted text exceeded max width then create a new line and add the remaining part of the text to the next line
                if len(formattedLine) + len(word) <= maxWidth:
                    formattedLine = formattedLine + str(word) + " "

                else:
                    # using rstrip to remove the space at the last
                    formattedLine = f'{formattedLine.rstrip(" ")}\n'
                    formattedText = formattedText + formattedLine.rstrip(" ")
                    formattedLine = indent + str(word) + " "
        else:
            formattedText = formattedText + line
        formattedText += formattedLine + "\n"
    return formattedText


if __name__ == '__main__':
    # rawText = "taskCpuUnlockNoResched - decrement lock counter without forcing a rescheduling event.\n\n This routine returns [OK] and removes the lock established using [taskCpuLock] but does not cause rescheduling.\n\nThis routine is similar to taskUnlock() or taskCpuUnlock() except this function does not cause a rescheduling event. Use of this function is reserved for the target debugger and the fair spinlock library that needs to unlock a task in critical sections where rescheduling is forbidden. \n\nThis routine is not callable from interrupt service routines. This is not enforced and it is the user's responsibility to adhere to this restriction. \n\nThe function decrements the preemption lock count of the current task."
    rawText = '''taskCreateWithGuard shall perform the following:<br/>    1. if [name] is equal to [NULL]:<br/>        1.1. set namelessPrefixLen to size in bytes of namelessPrefix<br/>        1.2. invoke [strncpy] with parameters newName, [namelessPrefix] and namelessPrefixLen, typecast the return value to void<br/>        1.3. set nBytes to the value returned from the invocation of [strnlen] with parameters newName and (size in bytes of newName)<br/>        1.4. set nPreBytes to nBytes <br/>        1.5. set value to (the result of the actions performed by inline function [vxAtomic32Inc] using value (address of [nameForNameless]), typecast the result to UINT32)<br/>        1.6. perform the following in the loop at least once:<br/>            1.6.1. set newName at index [nBytes incremented by one] to digits at index [value modulus by [TASK_TEN_VALUE]]<br/>            1.6.2. set value to the result of (value divided by [TASK_TEN_VALUE])<br/>            1.6.3. continue loop (step 1.6) while value is not equal to zero<br/>        1.7. set pBufStart to the sum of newName and nPreBytes<br/>        1.8. set pBufEnd to the result of (newName plus nBytes minus one)<br/>        1.9. perform the following while pBufStart is less than pBufEnd:<br/>            1.9.1. set temp to the first character of pBufStart<br/>            1.9.2. set the first character of pBufStart to the first character of pBufEnd<br/>            1.9.3. set the first character of pBufEnd to temp<br/>            1.9.4. decrement the (address of pointer pBufEnd) by one<br/>            1.9.5. increment the (address of pointer pBufStart) by one<br/>        1.10. set (character of newName at index nBytes) to [EOS]<br/>        1.11. set pointer [name] to pointer newName<br/>    2. set stackSizeRoundUp to [stackSize]<br/>    3. set stackSizeRoundUp to (the result of the actions performed by macro [STACK_ROUND_UP] using value stackSizeRoundUp, typecast the result to size_t)<br/>    4. if stackSizeRoundUp is less than [stackSize]:<br/>        4.1. perform the actions defined in macro [errno] and set the contents of memory (referenced by the result of the macro [errno]) to [S_taskLib_ILLEGAL_STACK_INFO]<br/>        4.2. return [TASK_ID_NULL]<br/>'''
    # rawText = "taskCreateWithGuard shall perform the following:\n    1. if [name] is equal to [NULL]:\n        - set namelessPrefixLen to size in bytes of namelessPrefix\n        - invoke [strncpy] with parameters newName, [namelessPrefix] and namelessPrefixLen, typecast the return value to void\n        1.6. perform the following in the loop at least once:\n            1.6.1. set newName at index [nBytes incremented by one] to digits at index [value modulus by [TASK_TEN_VALUE]]\n            1.6.2. set value to the result of (value divided by [TASK_TEN_VALUE])"
    for maxWidth in [60]:
        formattedText = formatRawText(rawText, maxWidth)
        print(formattedText)

