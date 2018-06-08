# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from orchestra.expressions import yql
from orchestra.tests.unit import base
from orchestra.utils import plugin


class YAQLEvaluationTest(base.ExpressionEvaluatorTest):

    @classmethod
    def setUpClass(cls):
        cls.language = 'yaql'
        super(YAQLEvaluationTest, cls).setUpClass()

    def test_get_evaluator(self):
        e = plugin.get_module(
            'orchestra.expressions.evaluators',
            self.language
        )

        self.assertEqual(e, yql.YAQLEvaluator)
        self.assertIn('json', e._custom_functions.keys())

    def test_custom_function(self):
        expr = '<% json(\'{"a": 123}\') %>'

        self.assertDictEqual({'a': 123}, self.evaluator.evaluate(expr))

    def test_custom_function_failure(self):
        expr = '<% json(int(123)) %>'

        self.assertRaises(
            yql.YaqlEvaluationException,
            self.evaluator.evaluate,
            expr
        )
