/*  find smaller elements on the right side and
greater elements on the left side for each element arr[i] in the given array. */



#include<iostream>
using namespace std;


int main(){
	
	int n;
	cout<<"enter number of elements: ";
	cin>>n;
	int arr[n];								//Array declaration
	
	cout<<endl<<"enter elements one by one: "<<endl;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}

	//2 arrays to keep track 
	int sm_r[n];							//smaller_right
	int gr_l[n];							//greater_left
	
	for(int i=0;i<n;i++){
		sm_r[i]=0;
		gr_l[i]=0;
		for(int j=i+1;j<n;j++){
			if(arr[j]<arr[i]){
				sm_r[i]++;
			}
		}
		
		for(int j=i;j>=0;j--){
			if(arr[j]>arr[i]){
				gr_l[i]++;
			}
		}
	}
	cout<<"Smaller right: ";				//Output display for Smaller Right
	for(int i=0;i<n;i++){
		cout<<sm_r[i]<<" ";	
	}
	
	cout<<endl<<"Greater left: ";			//Output display for Greater Left
	for(int i=0;i<n;i++){
		cout<<gr_l[i]<<" ";	
	}
	return 0;
}

