#include <iostream>
#include <vector>
using namespace std;
int main(){
    unsigned long int N,a;
    cin>>N;
    vector<int> v(N);
    for (unsigned long int i=0;i<N;i++){
        cin>>a;
        v[i]=a;
    }
    unsigned long int s=0;
    for (unsigned long int a=0;a<N-1;a++){
        unsigned long int s1=0;
        for (unsigned long int b=a+1;b<=N-1;b++){
            s1+=v[b];
        }
        s+=v[a]*s1;
    }
    cout<<s<<endl;
}