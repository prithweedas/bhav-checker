<template>
  <div v-if="data.length > 0">
    <div class="download">
      <button @click="downloadCsv()">
        <fa-icon icon="file-download" size="2x" />
      </button>
    </div>
    <div class="table">
      <table>
        <thead>
          <tr class="heading">
            <th>Code</th>
            <th>Name</th>
            <th>Open</th>
            <th>High</th>
            <th>Low</th>
            <th>Close</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in data" :key="item.code">
            <td>{{ item['code'] }}</td>
            <td>{{ item['name'] }}</td>
            <td>{{ item['open'] }}</td>
            <td>{{ item['high'] }}</td>
            <td>{{ item['low'] }}</td>
            <td>{{ item['close'] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-else class="no-data">
    <p>No data to show...</p>
  </div>
</template>

<script>
export default {
  name: 'Table',
  props: {
    data: Array
  },
  methods: {
    downloadCsv() {
      let content = 'data:text/csv;charset=utf-8,'
      content += 'Code,Name,Open,High,Low,Close\n'
      this.data.forEach((item) => {
        content += `${item['code']},${item['name']},${item['open']},${item['high']},${item['low']},${item['close']}\n`
      })
      const uri = encodeURI(content)
      const link = document.createElement('a')
      link.setAttribute('href', uri)
      link.setAttribute('download', 'search_results.csv')
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }
}
</script>

<style lang="scss" scoped>
.no-data {
  display: flex;
  justify-content: center;
  padding: 1rem;
  p {
    font-size: 2rem;
    color: #444;
  }
}

.download {
  display: flex;
  justify-content: flex-end;
  button {
    all: unset;
    color: #42b883;
    cursor: pointer;
  }
}

.table {
  display: flex;
  padding: 1rem 0;
  table {
    flex: 1;
    border-collapse: collapse;
    font-weight: bold;
    font-size: 1.5rem;
    td {
      text-align: center;
    }
    tr {
      height: 50px;
      background-color: #f6f3f7;
      border-bottom: rgba(0, 0, 0, 0.05) 1px solid;

      &.heading {
        height: 30px;
        background: #35495e;
        color: #ffffff;
        font-size: 1.2rem;
        border: 0px solid;
      }
    }
  }
}
</style>
