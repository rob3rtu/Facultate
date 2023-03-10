#include <bits/stdc++.h> 
using namespace std;
typedef pair< int,  int> pii;


vector<pii> points;
pii lefter, righter, top, bottom;
int l, r, t, b;

int main() {
    int n;
     int x, y;

    cin >> n;
    cin >> x >> y;
    lefter = make_pair(x, y);
    righter = lefter;
    top = lefter;
    bottom = lefter;

    points.push_back(lefter);

    for(int i = 1; i < n; i++) {
        cin >> x >> y;
        pii point = make_pair(x, y);

        if(point.first < lefter.first) {
            lefter = point;
            l = i;
        } 
         if(point.first > righter.first) {
            righter = point;
            r = i;
        } 
         if(point.second < bottom.second) {
            bottom = point;
            b = i;
        } 
         if(point.second > top.second) {
            top = point;
            t = i;
        }

        points.push_back(point);
    }
    points.push_back(points[0]);

    // cout << l << " " << t << " " << r << " " << b << '\n';
    // cout << "\n----------------------------\n\nX Monotonie 1:\n";

    bool xMonoton = true, yMonoton = true;

    //y monotonie

// cout << "\n----------------------------\n\nY Monotonie 1:\n";
    for(int i = b + 1; i % n != t; i++) {
        // cout << points[i].first << " " << points[i].second << '\n';
        if(points[i % n].second < points[i % n - 1].second) {
            // cout << "here\n";
            yMonoton = false;
            break;
        }
    }
    
// cout << "\n----------------------------\n\nY Monotonie 2:\n";
    if(yMonoton) 
        for(int i = b - 1; i != t; i--) 
            {
                if(i == -1) i = n - 1;
                if(i == t) break;
                // cout << points[i].first << " " << points[i].second << '\n';
                if(points[i].second < points[i + 1].second) {
                    // cout << "here\n";
                    yMonoton = false;
                    break;
                }
            }

    //x monotonie
    for(int i = l + 1; i % n != r; i++) {
        // cout << points[i].first << " " << points[i].second << '\n';
        if(points[i % n].first < points[(i % n) - 1].first) {
            // cout << "here\n";
            xMonoton = false;
            break;
        }
    }
        
    // cout << "\n----------------------------\n\nX Monotonie 2:\n";
    if(xMonoton) 
        for(int i = l - 1; i != r; i--) 
            {
                if(i == -1) i = n - 1;
                if(i == r) break;
                // cout << points[i].first << " " << points[i].second << '\n';
                if(points[i].first < points[i + 1].first) {
                    // cout << "here\n";
                    xMonoton = false;
                    break;
                }
            }
    
    


    cout << (xMonoton ? "YES\n" : "NO\n");
    cout << (yMonoton ? "YES\n" : "NO\n");

    return 0;
}