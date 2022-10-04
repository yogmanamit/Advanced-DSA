#include<bits/stdc++.h>
using namespace std;

//Drijksta Algorithm for shortest path using priority queue

int main(){
    int n,m,source;
    cin>>n>>m;
    vector<pair<int,int>>g[m+1];
    int a,b,wt;
    for(int i=0;i<m;i++){
        cin>>a>>b>>wt;
        g[a].push_back(make_pair(b,wt));
        g[b].push_back(make_pair(a,wt));
    }
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
    vector<int>distTo(n+1,INT_MAX);
    distTo[source]=0;
    pq.push(make_pair(0,source));
    while(!pq.empty()){
        int dist=pq.top().first;
        int prev=pq.top().second;
        pq.pop();
        vector<pair<int,int>>::iterator it;
        for(it=g[prev].begin();it!=g[prev].end();it++){
            int next=it->first;
            int nextDist=it->second;
            if(distTo[next]>distTo[prev]+nextDist){
                distTo[next]=distTo[prev]+nextDist;
                pq.push(make_pair(distTo[next],next));
            }
        }
    }
    for(int i=0;i<n;i++){
        cout<<distTo[i]<<" ";
    }
}
