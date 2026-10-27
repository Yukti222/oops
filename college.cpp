#include <iostream>
using namespace std;
class college {
    private:
    int roll_no,marks_of_maths;
    protected:
    float percent;
    public:
    void percent_of_maths(){
        cout<<"enter the marks of maths out of 70";
        cin>>marks_of_maths;
        percent=(marks_of_maths/70.0)*100;
        cout<<"the percentage of maths is: "<<percent<<endl;
    }
};
class AIML : public college{
    public:
    void eligibility(){
        if(percent>=75.0){
            cout<<"the student is eligible for AIML"<<endl;
        } 
        else {
            cout<<"the student is not eligible for AIML"<<endl;
        }
    }
};
int main(){
    AIML student;
    student.percent_of_maths();
    student.eligibility();
    return 0;
}