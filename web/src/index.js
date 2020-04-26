import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentDidMount() {
    axios.get('/api')
      .then(res => this.setState({
        api_response: res.data
      }))
  }

  render() {
    return (
      <div>
        <p>This is JSX from React!</p>
        <p>
          {
            this.state.api_response ?
              this.state.api_response :
              'Waiting...'
          }
        </p>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.querySelector('#root'));
