window.BENCHMARK_DATA = {
  "lastUpdate": 1607886075684,
  "repoUrl": "https://github.com/OpenMined/PySyft",
  "entries": {
    "Pytest-benchmarks": [
      {
        "commit": {
          "author": {
            "email": "anubhavraj.08@gmail.com",
            "name": "Anubhav Raj Singh",
            "username": "aanurraj"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "fe71a27a745d205981e44177d092d326f7e7c1af",
          "message": "add github benchmark-actions support (#4905)\n\n* added benchmark_actions support\r\n\r\n* added requirements\r\n\r\n* fixes\r\n\r\n* fixes\r\n\r\n* yml fixes\r\n\r\n* Trying different github secrets\r\n\r\n* Trying BENCHMARK_TOKEN\r\n\r\n* Changing token path\r\n\r\n* Trying different token setting\r\n\r\n* Back to secrets.GITHUB_TOKEN\r\n\r\nCo-authored-by: Madhava Jay <me@madhavajay.com>",
          "timestamp": "2020-12-13T15:19:24+10:00",
          "tree_id": "4959ab2de2e0399c8254a9e7c2e571e60235e71c",
          "url": "https://github.com/OpenMined/PySyft/commit/fe71a27a745d205981e44177d092d326f7e7c1af"
        },
        "date": 1607836891206,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/pytest_benchmarks/bench_test.py::test_string_serde",
            "value": 1897.024760214044,
            "unit": "iter/sec",
            "range": "stddev: 0.00007056849149450316",
            "extra": "mean: 527.141248218167 usec\nrounds: 842"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "OpenMined",
            "username": "OpenMined"
          },
          "committer": {
            "name": "OpenMined",
            "username": "OpenMined"
          },
          "id": "9b44f6775aea655bcf8cd6190672aadc859a69ac",
          "message": "PyDP Support",
          "timestamp": "2020-12-13T11:52:57Z",
          "url": "https://github.com/OpenMined/PySyft/pull/4908/commits/9b44f6775aea655bcf8cd6190672aadc859a69ac"
        },
        "date": 1607886075064,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/pytest_benchmarks/bench_test.py::test_string_serde",
            "value": 1054.763803145544,
            "unit": "iter/sec",
            "range": "stddev: 0.0002672168396321023",
            "extra": "mean: 948.0795577339438 usec\nrounds: 459"
          }
        ]
      }
    ]
  }
}