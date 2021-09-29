#problem: Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.

class sortMeetings(object):
    def mergeSort(self, meetings):
        #keep dividing by half until we hit the merge section
        if len(meetings) > 1:
            middle = len(meetings)//2
            left = meetings[:middle]
            right = meetings[middle:]

            self.mergeSort(left)
            self.mergeSort(right)

            #getting here implies the left and right are just single elements
            left_i = right_i = start_i = 0

            #until we either run out of elements on the left or right
            while left_i < len(left) and right_i < len(right):
                #if left is less than right, make it come before right, and
                #move left up by 1 since we've processed it or
                #do it for right if the opposite is true
                if left[left_i][0] < right[right_i][0]:
                    meetings[start_i] = left[left_i]
                    left_i+=1
                else:
                    meetings[start_i] = right[right_i]
                    right_i+=1
                start_i+=1

            #only one index will be left if the left and right arrays were uneven
            #since the only remaining elements should be > already added ones, we can just
            #tack them onto the list based on where we left off (start_i)
            while left_i<len(left):
                meetings[start_i]=left[left_i]
                left_i+=1
                start_i+=1

            while right_i<len(right):
                meetings[start_i]=right[right_i]
                right_i+=1
                start_i+=1


    def checkMeetings(self, meetings):
        #the logic is, sort the meetings by their starting times, line 34
        #and then iterate through them, if the end time of the current one is >
        # the start time of the next, their is a clear conflict
        self.mergeSort(meetings)
        x = 0
        while x < len(meetings)-1:
            if meetings[x][1] > meetings[x+1][0]:
                return False
            x+=1
        return True


a = [[15,20],[0,30],[5,10]]
c = [[7,10],[2,4]]
b = sortMeetings()
# b.mergeSort(a)
print(b.checkMeetings(a))
print(b.checkMeetings(c))
