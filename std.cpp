#include<bits/stdc++.h>
#include<windows.h>
using namespace std;
int main()
{
	int a,b,c,d=0;
	cin>>a>>b;
	for(int i=0;i<a;i++)
	{
		for(int j=0;j<b;j++)
		{
			cin>>c;
			d+=c;
		}
	}
	cout<<d;
	return 0;
}
