// no work!
#include <bits/stdc++.h> // <- not real library
using namespace std;
const int N = 100000;
vector<int> graph[N];
vector<int> cycles[N];
// &amp <- replace with &
void DFSCycle(int u, int p, int color[], int mark[], int par[], int&amp; cyclenumber){
   if (color[u] == 2) {
      return;
   }
   if (color[u] == 1) {
      cyclenumber++;
      int cur = p;
      mark[cur] = cyclenumber;
      while (cur != u) {
         cur = par[cur];
         mark[cur] = cyclenumber;
      }
      return;
   }
   par[u] = p;
   color[u] = 1;
   for (int v : graph[u]) {
      if (v == par[u]) {
         continue;
      }
      DFSCycle(v, u, color, mark, par, cyclenumber);
   }
   color[u] = 2;
}
void insert(int u, int v){
   graph[u].push_back(v);
   graph[v].push_back(u);
}
void printCycles(int edges, int mark[], int&amp; cyclenumber){
   for (int i = 1; i <= edges; i++) {
      if (mark[i] != 0)
         cycles[mark[i]].push_back(i);
   }
   for (int i = 1; i <= cyclenumber; i++) {
      cout << "Cycle " << i << ": ";
      for (int x : cycles[i])
         cout << x << " ";
      cout << endl;
   }
}
int main(){
   insert(1, 2);
   insert(2, 3);
   insert(3, 4);
   insert(4, 5);
   insert(5, 2);
   insert(5, 6);
   insert(6, 7);
   insert(7, 8);
   insert(6, 8);
   int color[N];
   int par[N];
   int mark[N];
   int cyclenumber = 0;
   cout<<"Cycles in the Graph are :\n";
   int edges = 13;
   DFSCycle(1, 0, color, mark, par, cyclenumber);
   printCycles(edges, mark, cyclenumber);
}