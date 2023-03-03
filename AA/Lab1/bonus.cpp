#include <bits/stdc++.h>
using namespace std;
typedef pair<long long, long long> pll;

vector<pll> points, hull;

long long getDet(pll a, pll b, pll c) {
    return b.first*c.second + a.first*b.second + c.first*a.second - 
           b.first*a.second - a.first*c.second - c.first*b.second;
}

double distance(pll a, pll b) {
    return sqrt((a.first - b.first)*(a.first - b.first) + 
                (a.second - b.second)*(a.second - b.second));
}

bool comparePoints(pll a, pll b) {
    return a.first < b.first || a.second < b.second;
}

bool compare(pll a, pll b) {
    long long o = getDet(points[0], a, b);

    if(o == 0) 
        return (distance(points[0], a) >= distance(points[0], b)) ? 0 : 1;

    return (o < 0) ? 0 : 1;
}

//sterge penultimul
void deleteLastLast(vector<pll> &v) {
    pll aux = v[ v.size() - 1 ];

    v.pop_back();
    v.pop_back();

    v.push_back(aux);
}

int main() {
    long long n, x, y, minY = INT_MAX, poz = 0;
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        if(y < minY || (y == minY && x < points[poz].first)) {
            minY = y;
            poz = i;
        }
        points.push_back(make_pair(x, y));
    }

    //bring the bootommost points first in the vector
    pll aux = points[0];
    points[0] = points[poz];
    points[poz] = aux;


    sort(points.begin() + 1, points.end(), compare);

    points.push_back(points[0]);
    hull.push_back(points[0]);
    hull.push_back(points[1]);

    for(int i = 2; i < points.size(); i++) {
        hull.push_back(points[i]);

        while(hull.size() > 2 && 
              getDet(hull[ hull.size() - 3 ],
                     hull[ hull.size() - 2 ],
                     hull[ hull.size() - 1 ] ) <= 0)   {
            deleteLastLast(hull);
        } 
    }

    // hull.pop_back();
    points.pop_back();

    // cout << '\n' << "CONVEX HULL" << '\n';
    // for(auto i : hull) {
    //     cout << i.first << " " << i.second << '\n';
    // }
    // cout << '\n';
    
    pll minR, minI, minJ;
    double minStep3 = LONG_MAX;

    while(hull.size() <= n) {
        minStep3 = LONG_MAX;

        for(auto point : points) {
            if(find(hull.begin(), hull.end(), point) == hull.end()) {
                pll r = point;
                double distMin = LONG_MAX;
                pll pi, pj;

                //finding pair(i, j) from Step 2
                for(int i = 0; i < hull.size() - 1; i++) {
                        double dist = distance(hull[i], r) + distance(r, hull[i + 1]) - distance(hull[i], hull[i + 1]);

                        //finding min r i j
                        if(dist < distMin) {
                            distMin = dist;
                            pi = hull[i];
                            pj = hull[i + 1];
                        }
                }

                double dist = (distance(pi, r) + distance(r, pj)) / distance(pi, pj);

                //finding min r* i* j*
                if(dist < minStep3) {
                    minStep3 = dist;
                    minR = r;
                    minI = pi;
                    minJ = pj;
                }
            }
        }

        // cout << "\nMinim r i j ->  (" << minR.first << " " << minR.second << "), (" << minI.first << " " << minI.second << ")," << minJ.first << " " << minJ.second << "),\n";

        hull.insert(find(hull.begin(), hull.end(), minI) + 1, minR);

        // cout << "\nNEW HULL\n";
        // for(auto p : hull) {
        // cout << p.first << " " << p.second;
        // cout << '\n';
        // }
    }


    // cout << '\n' << '\n';
    for(auto p : hull) {
        cout << p.first << " " << p.second << '\n';
    }

    return 0;
}