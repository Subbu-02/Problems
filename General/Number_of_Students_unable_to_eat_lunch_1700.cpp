class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        queue<int> q;
        for(int i=0; i<students.size(); i++){
            q.push(students[i]);
        }
        int count=0;
        int i=0;
        while(q.size()!=0)
        {
            if(q.front()==sandwiches[i])
            {
                q.pop();
                i++;
                count=0;
            }
            else
            {
                if(count>q.size())
                {
                    break;
                }
                int t = q.front();
                q.pop();
                q.push(t);
                count++;
            }
        }
        return q.size();
    }
};