#include <bits/stdc++.h>
using namespace std;

vector<int> solutie;
vector< pair<int, int> > intervale;

bool comp(pair<int, int> a, pair<int, int> b) {
    return a.first < b.first;
}

int main() {
    int a, b, n, x, y;

    cin >> a >> b >> n;

    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        intervale.push_back(make_pair(x, y));
    }

    sort(intervale.begin(), intervale.end(), comp);

    solutie.push_back(1);
    pair<int, int> last = intervale[0];

    for(int i = 0; i < n; i++) {
        // cout << "Last: " << last.first << " " << last.second << '\n';
        while(i < n - 1 && intervale[i + 1].first <= last.second) i++;

            solutie.push_back(i + 1);
            last = intervale[i];

            if(last.second >= b) break;
    }

    if( intervale[ solutie[0] - 1 ].first > a || 
        intervale[ solutie[ solutie.size() - 1 ] - 1 ].second < b ) {
            // cout << intervale[ solutie[0] - 1 ].first << " " << intervale[ solutie[ solutie.size() - 1 ] - 1 ].second;
            cout << 0;
            return 0;
    }

    for(int i = 0; i < solutie.size() - 1; i++) {
        if( intervale[ solutie[i] - 1 ].second < intervale[ solutie[i] ].first ) {
            cout << 0;
            return 0;
        }
    }

    cout << solutie.size() << '\n';

    for(int i : solutie) {
        cout << i << " ";
    }

    return 0;
}