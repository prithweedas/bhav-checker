<template>
  <div class="container">
    <SearchBox @search="onSearch" />
    <Table :data="bhavdata" />
  </div>
</template>

<script>
import SearchBox from './SearchBox'
import Table from './Table'
export default {
  name: 'Container',
  components: {
    SearchBox,
    Table
  },
  data() {
    return {
      bhavdata: []
    }
  },
  methods: {
    async onSearch(searchterm) {
      // INFO: in production will server the app through django
      const baseurl =
        process.env.NODE_ENV === 'development' ? 'http://localhost:8000' : ''
      try {
        const response = await fetch(`${baseurl}/api/search/`, {
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ search: searchterm }),
          method: 'POST'
        }).then((res) => res.json())
        this.bhavdata = response.data
      } catch (error) {
        // TODO: show some UI popup for errors
        console.log(error)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  flex: 1;
  display: flex;
  flex-direction: column;
  width: 80rem;
  padding: 0 1rem;
}
</style>
