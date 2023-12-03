```dataview
table w.wHome, w.wHomePast, w.wHomePastU, w.wHomeU where whereabout.wHome or displayDefaults.wHomePastU or displayDefaults.wHomePast or displayDefaults.wHomeU
```


```dataview
table displayDefaults.wCurrent, displayDefaults.wPast, displayDefaults.wLastKnown,displayDefaults.wLastKnownNoDate where displayDefaults.wCurrent or displayDefaults.wPast or displayDefaults.wLastKnown or displayDefaults.wLastKnownNoDate
```

```dataview
table displayDefaults.wOrigin, displayDefaults.wOriginU where displayDefaults.wOrigin or displayDefaults.wOriginU
```