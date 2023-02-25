#include <bits/stdc++.h>
using namespace std;
typedef pair<long long, long long> pii;

long long getDet(pii a, pii b, pii c) {
    return b.first*c.second + a.first*b.second + c.first*a.second - 
           b.first*a.second - a.first*c.second - c.first*b.second;
}

void deleteLastLast(vector<pii> &v) {
    pii aux = v[ v.size() - 1 ];

    v.pop_back();
    v.pop_back();

    v.push_back(aux);
}

vector<pii> points;
vector<pii> solutie;

int main() {
    long long n, x, y;

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        points.push_back(make_pair(x, y));
    }

    points.push_back(points[0]);
    solutie.push_back(points[0]);
    solutie.push_back(points[1]);

    for(int i = 2; i < points.size(); i++) {
        solutie.push_back(points[i]);

        while(solutie.size() > 2 && 
              getDet(solutie[ solutie.size() - 3 ],
                     solutie[ solutie.size() - 2 ],
                     solutie[ solutie.size() - 1 ] ) <= 0)   {
            deleteLastLast(solutie);
        } 
    }

    solutie.pop_back();
    cout << solutie.size() << '\n';

    for(auto sol : solutie) 
        cout << sol.first << " " << sol.second << '\n';

    return 0;
}