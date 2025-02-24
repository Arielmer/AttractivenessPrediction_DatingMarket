# ❤️ Predicting Attractiveness in Dating Markets

## 📌 Project Purpose
This project analyzes attractiveness and dating preferences using a **Speed Dating dataset from Columbia University (2002-2004)**. The study explores:
- ✅ Which factors contribute most to attractiveness?
- ✅ How do men and women differ in their dating preferences?
- ✅ How do ethnic groups interact in the dating scene?

---

## 📊 Dataset Description
The dataset consists of **8378 participants** from speed dating events. Below is a breakdown of the key features used in the analysis:

| **Feature**   | **Description**                                          |
|--------------|------------------------------------------------------|
| `fun3_3`    | Rating of partner’s fun (1-10)                     |
| `intel3_3`  | Rating of partner’s intelligence (1-10)            |
| `amb3_3`    | Rating of partner’s ambition (1-10)                |
| `sinc3_3`   | Rating of partner’s sincerity (1-10)               |
| `gender`    | 0 = Male, 1 = Female                                |
| `race`      | Participant's self-identified race                 |
| `race_o`    | Race of the partner they rated                     |
| `match`     | 1 if participants matched, 0 otherwise             |

---

## 🏷 Methodology
### 1️⃣ Data Collection
- The **Speed Dating dataset** from Columbia University (2002-2004) was used.
- Participants rated potential partners on **attractiveness, sincerity, intelligence, fun, ambition, and shared interests**.
- **Correlation analysis** was conducted to identify the strongest predictors of attractiveness.

### 2️⃣ Data Analysis
- **Correlation Matrix**: Features most strongly correlated with attractiveness were selected.
- **Regression models** were used to predict attractiveness based on selected features.
- **Box plots** were used to analyze gender-based preferences.
- **Heatmaps** were generated to study ethnic group interactions in dating.

### 3️⃣ Data Visualization
- **Feature importance in predicting attractiveness**.
- **Gender-based attractiveness ratings**.
- **Ethnic group interaction matrix**.

---

## 🔍 Key Findings & Insights
- **Factors influencing attractiveness**:
  - 🎉 Fun and intelligence contribute most to perceived attractiveness.
  - 📉 Ambition has a lesser impact compared to fun and sincerity.
- **Gender differences**:
  - 👨 Men prioritize attractiveness and fun more than women.
  - 👩 Women value intelligence and sincerity more.
- **Ethnic group interactions**:
  - 🖤 Black/African Americans rated Latinos highly.
  - 🔴 Native Americans favored Black and Latino partners.
  - 🟡 Asians showed the least preference for other Asians.

---

## 📊 Visualizations
### **Feature Importance in Predicting Attractiveness**
![Feature Importance](feature_importance.png)
- **Fun and intelligence are the strongest predictors of attractiveness, followed by sincerity and ambition.**
- **Correlation Analysis revealed that `fun3_3` had the highest positive correlation with attractiveness.**

### **Attractiveness Ratings by Gender**
![Gender Preferences](gender_attractiveness.png)
- **Men rated fun and attractiveness as more important, while women valued intelligence and sincerity higher.**
- **Correlation analysis indicated that men’s ratings of attractiveness correlated highly with fun ratings.**
- **Average attractiveness rating by men: 7.1, by women: 6.3**

### **Ethnic Group Interactions in Dating**
![Ethnic Preferences](ethnicity_interactions.png)
- **Black/African American participants preferred Latino partners, while Asians were least likely to prefer other Asians.**
- **Correlation analysis showed strong ethnic preferences that influenced match likelihood.**
- **Match rate between Black and Latino participants: 48%, Match rate between Asian participants: 15%**

---

## 🚀 Business & Social Implications
- **For individuals**: Provides data-driven insights into attractiveness trends.
- **For dating platforms**: Helps optimize matchmaking algorithms based on preferences and behavioral patterns.
- **For sociologists & researchers**: Offers a historical perspective on dating preferences and cultural shifts.

---

## 🛠 Technologies Used
- **Python**
  - pandas & numpy for data preprocessing
  - scikit-learn for regression modeling
  - matplotlib & seaborn for data visualization

---

## 📂 Repository Files
- **dating_market_analysis.py** – Script for data analysis and visualization.
- **Speed Dating Data.csv** – Dataset used in the analysis.
- **feature_importance.png** – Feature importance visualization.
- **gender_attractiveness.png** – Gender-based attractiveness rating analysis.
- **ethnicity_interactions.png** – Ethnic interaction match likelihood heatmap.
- **README.md** – Project documentation.

---

## 📢 Authors & Acknowledgments
- **Team 14A**: Ariel Liang, Brandon Phan, Hoonyoung Jung, Mingzhu Pan
- **Data Source**: Columbia University Speed Dating Experiment (2002-2004)
📂 **Presentation Link**: [Google Slides: Speed Dating Analysis](https://ucirvine-my.sharepoint.com/:p:/g/personal/ariel13_ad_uci_edu/Eb2LFynLVG5AotC6hpX_-28BDEV_NqqPXv5463A9BD7UPA?wdOrigin=TEAMS-WEB.undefined_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1740378730392&web=1)

For questions or contributions, feel free to reach out! 🚀






 
